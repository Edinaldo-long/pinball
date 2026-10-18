"""PINBALL NEON - pinball em Pygame (pip install pygame)

Controles
  Seta esquerda / Z  flipper esquerdo
  Seta direita / M   flipper direito
  ESPAÇO             segure para puxar o plunger, solte para lançar
  Seta para cima / X sacudir a mesa (3 vezes por bola)
  R                  reiniciar depois do fim de jogo
  ESC                sair

Dicas
  - Acenda os 5 alvos do topo: sobe o multiplicador e libera MULTIBOLA!
  - Os kickers (triângulos) perto dos flippers chutam a bola de volta.
  - Ganhe uma bola extra com 20.000 pontos.
"""
import math
import os
import random
import sys
from array import array

import pygame

W, H = 520, 780
TABLE_BOTTOM = 735
FPS = 60
SUBSTEPS = 6
GRAVITY = 0.33
BALL_R = 8
MAX_SPEED = 27

LANE_X0, LANE_X1 = 458, 500
LANE_FLOOR = 700

SCORE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pinball_recorde.txt")

# ---------------------------------------------------------------- geometria
def build_walls():
    walls = []
    cx, cy, r = 260, 260, 240
    n = 32
    pts = [(cx + r * math.cos(math.pi + math.pi * i / n),
            cy + r * math.sin(math.pi + math.pi * i / n)) for i in range(n + 1)]
    walls += list(zip(pts, pts[1:]))
    walls += [
        ((20, 260), (20, 590)),                 # parede esquerda
        ((500, 260), (500, TABLE_BOTTOM + 20)),  # parede direita da rampa
        ((458, 200), (458, TABLE_BOTTOM + 20)),  # divisória da rampa
        ((20, 590), (150, 665)),                # guia inferior esquerda
        ((458, 590), (328, 665)),               # guia inferior direita
    ]
    return walls, pts


WALLS, ARC_POINTS = build_walls()

SLINGS = [((50, 500), (110, 580)), ((428, 500), (368, 580))]

# x, y, raio, cor
BUMPERS = [
    (175, 250, 26, (255, 70, 120)),
    (303, 250, 26, (70, 220, 255)),
    (239, 335, 26, (255, 210, 70)),
    (85, 390, 18, (150, 255, 120)),
    (393, 390, 18, (190, 130, 255)),
]

TARGETS = [(129 + 55 * i, 160, 11) for i in range(5)]


def closest_point(p, a, b):
    abx, aby = b[0] - a[0], b[1] - a[1]
    t = ((p[0] - a[0]) * abx + (p[1] - a[1]) * aby) / (abx * abx + aby * aby)
    t = max(0.0, min(1.0, t))
    return a[0] + abx * t, a[1] + aby * t


def bounce_segment(ball, a, b, restitution=0.5, thickness=0.0, surf=None):
    """Colisão bola x segmento. Retorna (impacto, nx, ny) ou None."""
    px, py = ball["pos"]
    cx, cy = closest_point((px, py), a, b)
    dx, dy = px - cx, py - cy
    dist = math.hypot(dx, dy)
    rad = BALL_R + thickness
    if dist >= rad:
        return None
    if dist < 1e-6:
        nx, ny = 0.0, -1.0
    else:
        nx, ny = dx / dist, dy / dist
    ball["pos"][0] = cx + nx * rad
    ball["pos"][1] = cy + ny * rad
    sx, sy = surf((cx, cy)) if surf else (0.0, 0.0)
    rvx, rvy = ball["vel"][0] - sx, ball["vel"][1] - sy
    vn = rvx * nx + rvy * ny
    impact = 0.0
    if vn < 0:
        k = (1 + restitution) * vn
        rvx -= k * nx
        rvy -= k * ny
        ball["vel"][0] = rvx + sx
        ball["vel"][1] = rvy + sy
        impact = -vn
    return impact, nx, ny


def bounce_circle(ball, cx, cy, r, restitution=0.9, kick=0.0):
    dx, dy = ball["pos"][0] - cx, ball["pos"][1] - cy
    dist = math.hypot(dx, dy)
    if dist >= r + BALL_R or dist < 1e-6:
        return None
    nx, ny = dx / dist, dy / dist
    ball["pos"][0] = cx + nx * (r + BALL_R)
    ball["pos"][1] = cy + ny * (r + BALL_R)
    vn = ball["vel"][0] * nx + ball["vel"][1] * ny
    impact = 0.0
    if vn < 0:
        k = (1 + restitution) * vn
        ball["vel"][0] -= k * nx
        ball["vel"][1] -= k * ny
        ball["vel"][0] += nx * kick
        ball["vel"][1] += ny * kick
        impact = -vn
    return impact


# ------------------------------------------------------------------- sons
def make_sound(f0, f1, ms, vol=0.35, noise=0.0, square=False):
    rate = 44100
    n = int(rate * ms / 1000)
    buf = array("h")
    phase = 0.0
    for i in range(n):
        t = i / n
        phase += 2 * math.pi * (f0 + (f1 - f0) * t) / rate
        s = math.sin(phase)
        if square:
            s = 1.0 if s > 0 else -1.0
        s = s * (1 - noise) + random.uniform(-1, 1) * noise
        buf.append(int(s * (1 - t) ** 1.5 * vol * 32767))
    return pygame.mixer.Sound(buffer=buf.tobytes())


def load_sounds():
    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init(44100, -16, 1, 512)
        return {
            "bumper": make_sound(700, 1100, 110),
            "target": make_sound(900, 1500, 150, 0.2, square=True),
            "sling": make_sound(320, 150, 90, 0.4, noise=0.3),
            "flip": make_sound(140, 60, 60, 0.5, noise=0.4),
            "launch": make_sound(200, 700, 260),
            "drain": make_sound(500, 70, 700, 0.4),
            "bonus": make_sound(500, 1800, 600, 0.25, square=True),
        }
    except Exception:
        return {}


# ------------------------------------------------------------------ flipper
class Flipper:
    LENGTH = 78
    SPEED = 0.30  # rad/frame

    def __init__(self, pivot, rest_deg, up_deg):
        self.pivot = pivot
        self.rest = math.radians(rest_deg)
        self.up = math.radians(up_deg)
        self.angle = self.rest
        self.omega = 0.0

    def step(self, pressed, frac):
        target = self.up if pressed else self.rest
        m = self.SPEED * frac
        d = max(-m, min(m, target - self.angle))
        self.angle += d
        self.omega = d / frac

    @property
    def tip(self):
        return (self.pivot[0] + math.cos(self.angle) * self.LENGTH,
                self.pivot[1] + math.sin(self.angle) * self.LENGTH)

    def surface_velocity(self, p):
        rx, ry = p[0] - self.pivot[0], p[1] - self.pivot[1]
        return -self.omega * ry, self.omega * rx


# --------------------------------------------------------------------- jogo
def new_ball(x, y, vx=0.0, vy=0.0):
    return {"pos": [float(x), float(y)], "vel": [vx, vy], "trail": []}


class Game:
    def __init__(self, sounds=True):
        self.sfx = load_sounds() if sounds else {}
        self.high = self.load_high()
        self.left = Flipper((150, 665), 30, -30)
        self.right = Flipper((328, 665), 150, 210)
        self.reset()

    # ---- estado
    def reset(self):
        self.score = 0
        self.lives = 3
        self.mult = 1
        self.lit = [False] * len(TARGETS)
        self.balls = []
        self.charge = 0.0
        self.nudges = 3
        self.over = False
        self.extra_given = False
        self.prev_l = self.prev_r = False
        self.flash = {}
        self.particles = []
        self.texts = []
        self.spawn_lane_ball()

    def spawn_lane_ball(self):
        self.balls.append(new_ball(479, LANE_FLOOR - BALL_R - 2))
        self.nudges = 3

    def play(self, name):
        s = self.sfx.get(name)
        if s:
            s.play()

    @staticmethod
    def load_high():
        try:
            with open(SCORE_FILE) as f:
                return int(f.read().strip())
        except Exception:
            return 0

    def save_high(self):
        try:
            with open(SCORE_FILE, "w") as f:
                f.write(str(self.high))
        except Exception:
            pass

    # ---- efeitos
    def add_score(self, pts, x, y, color=(255, 255, 255)):
        total = pts * self.mult
        self.score += total
        self.texts.append({"t": f"+{total}", "x": x, "y": y, "life": 40, "c": color})
        if not self.extra_given and self.score >= 20000:
            self.extra_given = True
            self.lives += 1
            self.say("BOLA EXTRA!", (255, 230, 80))
            self.play("bonus")

    def say(self, text, color=(255, 255, 255)):
        self.texts.append({"t": text, "x": 239, "y": 440, "life": 90, "c": color, "big": True})

    def burst(self, x, y, color, n=10):
        for _ in range(n):
            a = random.uniform(0, math.tau)
            s = random.uniform(1, 4)
            self.particles.append({"x": x, "y": y, "vx": math.cos(a) * s, "vy": math.sin(a) * s,
                                   "life": random.randint(15, 30), "c": color})

    # ---- entrada
    def lane_balls(self):
        return [b for b in self.balls if b["pos"][0] > LANE_X0 and b["pos"][1] > LANE_FLOOR - 70]

    def release(self):
        if self.over:
            return
        if self.charge > 0:
            power = self.charge
            for b in self.lane_balls():
                b["vel"][1] = -(10 + 17 * power)
                b["vel"][0] = 0
            self.play("launch")
        self.charge = 0.0

    def nudge(self):
        if self.over or self.nudges <= 0:
            return
        moving = [b for b in self.balls if b not in self.lane_balls()]
        if not moving:
            return
        self.nudges -= 1
        for b in moving:
            b["vel"][0] += random.uniform(-2, 2)
            b["vel"][1] -= random.uniform(1.5, 3)
        self.play("sling")

    # ---- atualização
    def update(self, left, right, charging):
        self.update_fx()
        if self.over:
            return
        if left and not self.prev_l:
            self.play("flip")
        if right and not self.prev_r:
            self.play("flip")
        self.prev_l, self.prev_r = left, right

        if charging and self.lane_balls():
            self.charge = min(1.0, self.charge + 0.022)

        frac = 1.0 / SUBSTEPS
        for _ in range(SUBSTEPS):
            self.left.step(left, frac)
            self.right.step(right, frac)
            for b in self.balls:
                self.step_ball(b, frac)
            self.ball_vs_ball()

        for b in self.balls[:]:
            b["trail"].append((b["pos"][0], b["pos"][1]))
            if len(b["trail"]) > 10:
                b["trail"].pop(0)
            if b["pos"][1] > TABLE_BOTTOM + BALL_R:
                self.balls.remove(b)

        if not self.balls:
            self.lives -= 1
            self.play("drain")
            if self.lives <= 0:
                self.over = True
                if self.score > self.high:
                    self.high = self.score
                    self.save_high()
            else:
                self.mult = 1
                self.spawn_lane_ball()

    def step_ball(self, b, frac):
        b["vel"][1] += GRAVITY * frac
        sp = math.hypot(*b["vel"])
        if sp > MAX_SPEED:
            b["vel"][0] *= MAX_SPEED / sp
            b["vel"][1] *= MAX_SPEED / sp
        b["pos"][0] += b["vel"][0] * frac
        b["pos"][1] += b["vel"][1] * frac

        for a, c in WALLS:
            bounce_segment(b, a, c, 0.35)

        # chão do plunger (desce quando puxado)
        floor = LANE_FLOOR + self.charge * 22
        if b["pos"][1] <= floor:  # só colide por cima (a bola sobe livre ao lançar)
            bounce_segment(b, (LANE_X0, floor), (LANE_X1, floor), 0.0)

        # portão de mão única: impede a bola de voltar para a rampa
        if b["vel"][0] > 0 and b["pos"][0] < LANE_X0 + 1:
            bounce_segment(b, (LANE_X0, 118), (LANE_X0, 200), 0.4)

        for fl in (self.left, self.right):
            bounce_segment(b, fl.pivot, fl.tip, 0.35, 5, fl.surface_velocity)

        for i, (a, c) in enumerate(SLINGS):
            r = bounce_segment(b, a, c, 0.5, 2)
            if r and r[0] > 1.0:
                b["vel"][0] += r[1] * 5
                b["vel"][1] += r[2] * 5
                self.flash[("s", i)] = 8
                self.add_score(50, b["pos"][0], b["pos"][1], (255, 160, 90))
                self.burst(b["pos"][0], b["pos"][1], (255, 160, 90), 6)
                self.play("sling")

        for i, (x, y, r, col) in enumerate(BUMPERS):
            imp = bounce_circle(b, x, y, r, 0.9, 4.5)
            if imp and imp > 0.2:
                self.flash[("b", i)] = 8
                self.add_score(100, x, y - r, col)
                self.burst(x, y, col)
                self.play("bumper")

        for i, (x, y, r) in enumerate(TARGETS):
            imp = bounce_circle(b, x, y, r, 0.6)
            if imp and imp > 0.2 and not self.lit[i]:
                self.lit[i] = True
                self.flash[("t", i)] = 10
                self.add_score(500, x, y + 22, (255, 240, 120))
                self.burst(x, y, (255, 240, 120), 8)
                self.play("target")
                if all(self.lit):
                    self.targets_complete()

    def targets_complete(self):
        self.lit = [False] * len(TARGETS)
        self.mult = min(5, self.mult + 1)
        self.add_score(2500, 239, 190, (255, 240, 120))
        self.say(f"MULTIBOLA!  x{self.mult}", (120, 255, 200))
        self.play("bonus")
        self.balls.append(new_ball(239, 105, random.uniform(-2, 2), 3))

    def ball_vs_ball(self):
        bs = self.balls
        for i in range(len(bs)):
            for j in range(i + 1, len(bs)):
                a, c = bs[i], bs[j]
                dx, dy = c["pos"][0] - a["pos"][0], c["pos"][1] - a["pos"][1]
                d = math.hypot(dx, dy)
                if 0 < d < 2 * BALL_R:
                    nx, ny = dx / d, dy / d
                    over = (2 * BALL_R - d) / 2
                    a["pos"][0] -= nx * over
                    a["pos"][1] -= ny * over
                    c["pos"][0] += nx * over
                    c["pos"][1] += ny * over
                    vn = (a["vel"][0] - c["vel"][0]) * nx + (a["vel"][1] - c["vel"][1]) * ny
                    if vn > 0:
                        a["vel"][0] -= vn * nx
                        a["vel"][1] -= vn * ny
                        c["vel"][0] += vn * nx
                        c["vel"][1] += vn * ny

    def update_fx(self):
        for k in list(self.flash):
            self.flash[k] -= 1
            if self.flash[k] <= 0:
                del self.flash[k]
        for p in self.particles[:]:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["vy"] += 0.1
            p["life"] -= 1
            if p["life"] <= 0:
                self.particles.remove(p)
        for t in self.texts[:]:
            t["y"] -= 0.6
            t["life"] -= 1
            if t["life"] <= 0:
                self.texts.remove(t)


# ------------------------------------------------------------------ desenho
class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.f_small = pygame.font.SysFont("arial", 15, bold=True)
        self.f_mid = pygame.font.SysFont("arial", 22, bold=True)
        self.f_big = pygame.font.SysFont("arial", 34, bold=True)
        self.bg = self.make_bg()

    @staticmethod
    def make_bg():
        s = pygame.Surface((W, H))
        for y in range(H):
            k = y / H
            pygame.draw.line(s, (int(10 + 18 * k), int(8 + 6 * k), int(30 + 30 * k)), (0, y), (W, y))
        poly = ARC_POINTS + [(500, TABLE_BOTTOM), (20, TABLE_BOTTOM)]
        pygame.draw.polygon(s, (24, 18, 58), poly)
        # decoração: círculos e estrelas suaves
        rnd = random.Random(7)
        for _ in range(40):
            x, y = rnd.randint(30, 450), rnd.randint(40, 700)
            pygame.draw.circle(s, (40, 32, 90), (x, y), rnd.randint(1, 3))
        pygame.draw.circle(s, (32, 26, 74), (239, 440), 70, 2)
        pygame.draw.circle(s, (32, 26, 74), (239, 440), 45, 2)
        return s

    def txt(self, font, text, color, center=None, topleft=None, alpha=255):
        img = font.render(text, True, color)
        if alpha < 255:
            img.set_alpha(alpha)
        r = img.get_rect()
        if center:
            r.center = center
        if topleft:
            r.topleft = topleft
        self.screen.blit(img, r)

    def draw(self, g):
        sc = self.screen
        sc.blit(self.bg, (0, 0))

        # paredes com brilho
        for a, c in WALLS:
            pygame.draw.line(sc, (40, 60, 140), a, c, 7)
        for a, c in WALLS:
            pygame.draw.line(sc, (120, 170, 255), a, c, 2)

        # kickers
        for i, (a, c) in enumerate(SLINGS):
            on = g.flash.get(("s", i), 0) > 0
            col = (255, 190, 100) if on else (255, 120, 60)
            third = (a[0], c[1]) if a[0] < 239 else (a[0], c[1])
            pygame.draw.polygon(sc, (70, 30, 40), [a, c, third])
            pygame.draw.line(sc, col, a, c, 6 if on else 4)

        # alvos
        for i, (x, y, r) in enumerate(TARGETS):
            if g.lit[i]:
                pygame.draw.circle(sc, (255, 240, 120), (x, y), r + 4, 2)
                pygame.draw.circle(sc, (255, 240, 120), (x, y), r)
            else:
                pygame.draw.circle(sc, (70, 66, 120), (x, y), r)
                pygame.draw.circle(sc, (160, 160, 220), (x, y), r, 2)
            if g.flash.get(("t", i), 0) > 0:
                pygame.draw.circle(sc, (255, 255, 255), (x, y), r + 8, 2)

        # bumpers
        for i, (x, y, r, col) in enumerate(BUMPERS):
            on = g.flash.get(("b", i), 0) > 0
            dark = tuple(int(v * 0.35) for v in col)
            pygame.draw.circle(sc, dark, (x, y), r + (6 if on else 3))
            pygame.draw.circle(sc, col if not on else (255, 255, 255), (x, y), r - 2)
            pygame.draw.circle(sc, (255, 255, 255), (x, y), r - 2, 2)
            pygame.draw.circle(sc, dark, (x, y), r // 2)

        # plunger
        floor = int(LANE_FLOOR + g.charge * 22)
        pygame.draw.rect(sc, (200, 200, 220), (LANE_X0 + 8, floor, 26, 6))
        for k in range(6):
            yy = floor + 8 + k * ((TABLE_BOTTOM - floor - 8) / 6)
            pygame.draw.line(sc, (120, 120, 160), (LANE_X0 + 10, yy), (LANE_X0 + 32, yy), 2)
        if g.charge > 0:
            w = int(30 * g.charge)
            pygame.draw.rect(sc, (255, int(255 - 200 * g.charge), 60), (LANE_X0 + 6, TABLE_BOTTOM - 4, w, 4))

        # flippers
        for fl in (g.left, g.right):
            pygame.draw.line(sc, (60, 40, 10), fl.pivot, fl.tip, 14)
            pygame.draw.line(sc, (255, 200, 60), fl.pivot, fl.tip, 10)
            pygame.draw.circle(sc, (255, 240, 160), fl.pivot, 6)

        # bolas e rastro
        for b in g.balls:
            for i, (tx, ty) in enumerate(b["trail"]):
                rr = max(1, int(BALL_R * (i + 1) / len(b["trail"]) * 0.8))
                v = 60 + 12 * i
                pygame.draw.circle(sc, (v // 2, v // 2, v), (int(tx), int(ty)), rr)
            x, y = int(b["pos"][0]), int(b["pos"][1])
            pygame.draw.circle(sc, (200, 210, 230), (x, y), BALL_R)
            pygame.draw.circle(sc, (255, 255, 255), (x - 2, y - 3), 3)

        # partículas e textos
        for p in g.particles:
            pygame.draw.circle(sc, p["c"], (int(p["x"]), int(p["y"])), 2)
        for t in g.texts:
            font = self.f_big if t.get("big") else self.f_small
            self.txt(font, t["t"], t["c"], center=(t["x"], t["y"]), alpha=min(255, t["life"] * 12))

        if g.lane_balls() and len(g.balls) == len(g.lane_balls()) and not g.over:
            self.txt(self.f_small, "Segure ESPAÇO e solte para lançar", (255, 220, 120), center=(239, 500))

        self.draw_panel(g)
        if g.over:
            self.draw_game_over(g)

    def draw_panel(self, g):
        sc = self.screen
        pygame.draw.rect(sc, (12, 10, 30), (0, TABLE_BOTTOM, W, H - TABLE_BOTTOM))
        pygame.draw.line(sc, (120, 170, 255), (0, TABLE_BOTTOM), (W, TABLE_BOTTOM), 2)
        fmt = lambda n: f"{n:,}".replace(",", ".")
        self.txt(self.f_small, "PONTOS", (140, 150, 200), topleft=(16, TABLE_BOTTOM + 6))
        self.txt(self.f_mid, fmt(g.score), (255, 255, 255), topleft=(16, TABLE_BOTTOM + 21))
        self.txt(self.f_small, "RECORDE", (140, 150, 200), topleft=(180, TABLE_BOTTOM + 6))
        self.txt(self.f_mid, fmt(max(g.high, g.score)), (255, 220, 100), topleft=(180, TABLE_BOTTOM + 21))
        self.txt(self.f_small, f"MULT x{g.mult}", (120, 255, 200), topleft=(330, TABLE_BOTTOM + 6))
        self.txt(self.f_small, f"SACUDIR (↑): {g.nudges}", (140, 150, 200), topleft=(330, TABLE_BOTTOM + 28))
        for i in range(max(0, g.lives)):
            pygame.draw.circle(sc, (220, 225, 240), (440 + i * 18, TABLE_BOTTOM + 14), 6)

    def draw_game_over(self, g):
        veil = pygame.Surface((W, H), pygame.SRCALPHA)
        veil.fill((0, 0, 0, 170))
        self.screen.blit(veil, (0, 0))
        self.txt(self.f_big, "FIM DE JOGO", (255, 100, 120), center=(W // 2, 300))
        self.txt(self.f_mid, f"Pontos: {g.score:,}".replace(",", "."), (255, 255, 255), center=(W // 2, 350))
        if g.score >= g.high and g.score > 0:
            self.txt(self.f_mid, "NOVO RECORDE!", (255, 220, 100), center=(W // 2, 385))
        self.txt(self.f_small, "Pressione R para jogar de novo", (200, 210, 255), center=(W // 2, 430))


def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Pinball Neon")
    clock = pygame.time.Clock()
    game = Game()
    rend = Renderer(screen)
    charging = False

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    charging = True
                elif e.key in (pygame.K_UP, pygame.K_x):
                    game.nudge()
                elif e.key == pygame.K_r and game.over:
                    game.reset()
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                charging = False
                game.release()

        k = pygame.key.get_pressed()
        game.update(k[pygame.K_LEFT] or k[pygame.K_z], k[pygame.K_RIGHT] or k[pygame.K_m], charging)
        rend.draw(game)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()