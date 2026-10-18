<div align="center">

# ⚡ NEON PINBALL ARCADE

### *Simulação Física de Alta Fidelidade • Síntese de Áudio Procedural • Gráficos Vetoriais Puros*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.5+-FFE873?style=for-the-badge&logo=python&logoColor=3776AB)](https://www.pygame.org/)
[![Physics](https://img.shields.io/badge/Physics-Custom_Sub--Stepping-f43f5e?style=for-the-badge&logo=target)](https://github.com/Edinaldo-long/pinball)
[![Audio](https://img.shields.io/badge/Audio-Procedural_PCM-38bdf8?style=for-the-badge&logo=soundcloud)](https://github.com/Edinaldo-long/pinball)
[![License](https://img.shields.io/badge/License-MIT-c084fc?style=for-the-badge)](LICENSE)

<br/>



<p align="center">
  <b>Uma mesa completa de Pinball retro-arcade com física de corpos rígidos vetorial implementada do zero em Python nativo, sem motores externos como Box2D ou Pymunk, e sem recurso a ficheiros de áudio ou sprites externos.</b>
</p>

[🎮 Controlos](#-controlos) • [🔬 Engenharia & Físicas](#-arquitetura-e-engenharia-de-física) • [🕹️ Regras da Mesa](#-regras-e-pontuação) • [🚀 Instalação](#-como-executar)

---

</div>

## 🌟 Visão Geral do Projeto

O **Neon Pinball** recria a dinâmica real de uma máquina eletromecânica de flippers dos anos 80/90. O diferencial deste projeto reside na sua **independência de assets externos**: todos os elementos visuais, curvaturas de rampa, colisores, partículas incandescentes e sons de impacto são calculados e gerados proceduralmente por código matemático em tempo de execução[cite: 5].

---

## 🔬 Arquitetura e Engenharia de Física

### 1. ⚙️ Pipeline Física com Sub-Stepping (Anti-Tunneling)
Bolas de pinball atingem velocidades de pico elevadas (`MAX_SPEED = 27 px/frame`)[cite: 5]. Em motores físicos a 60 FPS, isso causaria o efeito de *tunneling* (a bola atravessar paredes ou flippers entre fotogramas consecutivos).
* **Solução:** O ciclo principal divide cada fotograma em **6 sub-passos temporais discretos** (`SUBSTEPS = 6`), elevando a taxa de amostragem interna para **360 Hz**[cite: 5].
* A integração das equações de Euler modificadas assegura trajetórias estáveis e colisões contínuas mesmo durante impactos elásticos de alta intensidade.

### 2. 🕹️ Cinemática Rotacional dos Flippers
Os batentes (flippers) não atuam apenas como defletores geométricos estáticos:
* O sistema calcula a **velocidade angular instantânea** ($\omega = \frac{\Delta\theta}{\Delta t}$) da ponta e do corpo do flipper[cite: 5].
* No momento do contacto, a velocidade superficial tangencial é calculada vetorialmente[cite: 5]:
  $$\vec{v}_{\text{superfície}} = (-\omega \cdot r_y, \; \omega \cdot r_x)$$
* Essa velocidade é transferida diretamente como momento linear adicional para a bola, permitindo tacadas calculadas, amortecimentos suaves e disparos com base no tempo de acionamento[cite: 5].

### 3. 🔊 Síntese Procedural de Áudio (DSP por Software)
Nenhum ficheiro `.wav` ou `.mp3` é necessário no repositório. O jogo sintetiza som diretamente na memória RAM através do módulo nativo `array` do Python[cite: 5]:
* **Bumpers & Plunger:** Modulação de frequência por chirp senoidal ($f_0 \to f_1$) combinada com decaimento exponencial de envelope ($e^{-kt}$)[cite: 5].
* **Flippers & Slingshots:** Injeção controlada de ruído pseudo-aleatório (ruído branco filtrado) misturado com frequências graves para simular o solenoide mecânico[cite: 5].
* **Alvos e Bónus:** Ondas quadradas harmónicas sintetizadas por software para timbres característicos de chips de som vintage[cite: 5].

### 4. 🧮 Geometria Analítica e Deteção Contínua
* **Projeção Escalar em Segmentos:** Cálculo parametrizado $t \in [0, 1]$ para deteção precisa em paredes lineares e guias angulares[cite: 5].
* **Colisão Elástica Esfera-contra-Esfera (Multibola):** Resolução de sobreposição geométrica com conservação de momento linear nos eixos normais de impacto[cite: 5].

---

## 🎮 Controlos

| Comando | Tecla Teclado | Efeito Mecânico |
| :--- | :--- | :--- |
| **Flipper Esquerdo** | <kbd>Seta Esquerda</kbd> ou <kbd>Z</kbd> | Aciona o flipper esquerdo com rotação acelerada |
| **Flipper Direito** | <kbd>Seta Direita</kbd> ou <kbd>M</kbd> | Aciona o flipper direito com rotação acelerada |
| **Mola de Lançamento** | <kbd>Barra de Espaço</kbd> | **Segure** para tensionar a mola; **solte** para disparar |
| **Sacudir Mesa (Nudge)** | <kbd>Seta para Cima</kbd> ou <kbd>X</kbd> | Aplica aceleração caótica (máximo de 3 vezes por bola) |
| **Reiniciar Partida** | <kbd>R</kbd> | Reinicia a mesa após o ecrã de Fim de Jogo |
| **Sair** | <kbd>ESC</kbd> | Encerra a aplicação |

---

## 🕹️ Regras e Pontuação

```text
┌────────────────────────────────────────────────────────────────────────┐
│                          TABELA DE PONTUAÇÃO                           │
├──────────────────────────┬──────────────┬──────────────────────────────┤
│ Elemento                 │ Pontos       │ Efeito Especial              │
├──────────────────────────┼──────────────┼──────────────────────────────┤
│ Bumpers Centrais         │ 100 × Mult   │ Impulso elástico radial +4.5 │
│ Kickers / Slingshots     │ 50 × Mult    │ Repulsão angular rápida      │
│ Alvos Superiores (x5)    │ 500 × Mult   │ Ilumina indicador neon       │
│ Combo Todos os 5 Alvos   │ +2.500 Pts   │ Aumenta Mult e MULTIBOLA     │
│ Bola Extra               │ Aos 20.000   │ +1 Vida adicional            │
└──────────────────────────┴──────────────┴──────────────────────────────┘
