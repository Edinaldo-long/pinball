
Gemini

Novo chat
Biblioteca
Imagens
Agendado
Estudantes

Mais
Novo notebook
Untitled notebook
Untitled notebook
Ponto Cego: Liberdade e Vida Extraordinária
Guia para Publicar Jogo no GitHub
Controle USB para Pygame e Flutter
Análise do Comando Knup KP-CN701/S
Escolha de Controle para Jogos
Verificação De Meia De Compressão
Kotlin vs. Flutter: Diferenças
Viabilidade de QR Code no Estoque
U2 Mysterious Ways e a palavra freira
README para Jogo Flame 2D
Sem nome
Avaliação do Tamanho da Meia
Controles USB Baratos para PC
Símbolos Maçônicos no Garment Mórmon
Stacks Mais Demandadas no Mercado
Filmes brasileiros sobre tráfico e favelas
Publicar Index no Firebase Hosting
O que é uma lista em programação?
Cirurgia em Tartarugas e Quelônios
Entendendo o Long Jack 10:1
Exploração da Lua e Marte
Conversa com o Gemini
PS C:\Users\esata\argolas_aquaticas> python argolas_aquaticas.py

pygame 2.6.1 (SDL 2.28.4, Python 3.11.1)

Hello from the pygame community. https://www.pygame.org/contribute.html

PS C:\Users\esata\argolas_aquaticas> 

 *  History restored 



PS C:\Users\esata\argolas_aquaticas> git init

>> git remote add origin https://github.com/Edinaldo-long/argolas-aquaticas.git

>> git pull origin main

Initialized empty Git repository in C:/Users/esata/argolas_aquaticas/.git/

remote: Enumerating objects: 3, done.

remote: Counting objects: 100% (3/3), done.

remote: Compressing objects: 100% (2/2), done.

remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)

Unpacking objects: 100% (3/3), 1.45 KiB | 1024 bytes/s, done.

From https://github.com/Edinaldo-long/argolas-aquaticas

 * [new branch]      main       -> origin/main

PS C:\Users\esata\argolas_aquaticas> git add .

>> git commit -m "feat: adicionar jogo argolas aquáticas e documentação"

>> git branch -M main

>> git push -u origin main

[master 64fc0f0] feat: adicionar jogo argolas aquáticas e documentação

 2 files changed, 853 insertions(+)

 create mode 100644 argolas_aquaticas.py

 create mode 100644 argolas_recorde.txt

Enumerating objects: 5, done.

Counting objects: 100% (5/5), done.

Delta compression using up to 4 threads

Compressing objects: 100% (3/3), done.

Writing objects: 100% (4/4), 10.23 KiB | 1.71 MiB/s, done.

Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)

To https://github.com/Edinaldo-long/argolas-aquaticas.git

   066604b..64fc0f0  main -> main

branch 'main' set up to track 'origin/main'.

PS C:\Users\esata\argolas_aquaticas> 

O envio para o GitHub foi concluído com sucesso! O código do jogo já se encontra no repositório remoto na ramificação main.   
PY
+ 1

Para deixar o repositório pronto e com apresentação profissional para o seu portfólio, restam apenas dois ajustes: adicionar os ficheiros de documentação (README.md e requirements.txt) e remover do controlo de versões o ficheiro de recorde local (argolas_recorde.txt), que foi enviado no primeiro envio.   
PY

Passo 1: Remover o ficheiro de recorde do rastreio do Git
Para retirar o argolas_recorde.txt do repositório remoto sem o apagar do seu computador:

PowerShell
git rm --cached argolas_recorde.txt
Passo 2: Criar os ficheiros auxiliares
Na mesma pasta C:\Users\esata\argolas_aquaticas, crie os seguintes três ficheiros:

.gitignore

Plaintext
__pycache__/
*.py[cod]
.venv/
venv/
argolas_recorde.txt
.vscode/
requirements.txt

Plaintext
pygame>=2.5.0
README.md

(Copie e cole o modelo estruturado de apresentação e documentação sugerido anteriormente).

Passo 3: Enviar as alterações para o GitHub
No terminal do PowerShell, execute:

PowerShell
git add .
git commit -m "docs: adicionar README, requirements e ignorar recorde local"
git push
Como verificar: Aceda à página do seu repositório no navegador ([https://github.com/Edinaldo-long/argolas-aquaticas](https://github.com/Edinaldo-long/argolas-aquaticas)) e atualize a página (F5). O README.md deverá aparecer imediatamente formatado na página inicial e o ficheiro argolas_recorde.txt não constará mais da lista de ficheiros.   
PNG

preciso de um read me bem legal

Vou gerar agora um arquivo README.md completo, atraente e formatado com badges, seções técnicas detalhadas e estrutura de portfólio para destacar o seu projeto no GitHub.

README.md
18/10, 15:06
Criei um README.md completo, com badges, tabela de regras e controles, além da explicação técnica da física e do gerador procedural de som.

Para adicioná-lo ao seu projeto:

Salve o arquivo acima com o nome README.md dentro da pasta C:\Users\esata\argolas_aquaticas.

Crie uma pasta chamada screenshots, tire uma foto da janela do jogo rodando e salve como gameplay.png dentro dela.

No terminal, envie a atualização:

PowerShell
   git add .
   git commit -m "docs: adicionar documentacao completa no README"
   git push
   
quero em html por favor

Vou criar uma página HTML completa, interativa e estilizada para o seu portfólio, contendo a apresentação do jogo, detalhes técnicos, controles, showcase visual e links para o repositório.

Portfolio - Argolas Aquáticas
18/10, 14:20
Gerei o arquivo index.html com:

Design Marinho & Retrô: Paleta de cores subaquáticas, efeitos de transparência (glassmorphism) e bolhas geradas via CSS.

Showcase Visual do Jogo: Uma representação ilustrada do aquário com pinos e argolas coloridas simulando a interface.

Documentação de Engenharia: Detalhamento da física de fluidos, geração procedural de áudio por buffers senoidais e tabelas completas de regras e controles.

Responsividade e Integração: Funciona em celulares e desktops, com links diretos para o seu perfil e repositório Edinaldo-long/argolas-aquaticas.

Você pode salvar esse arquivo no repositório e ativá-lo gratuitamente via GitHub Pages (em Settings > Pages) para ter um site online no seu portfólio!

me de o codigo por favor em html

O seu arquivo HTML está pronto para download e visualização:

Ícone de HTML
index
 HTML 
Aqui está o código-fonte completo em HTML + CSS inline para copiar diretamente para o seu projeto:

HTML
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Argolas Aquáticas - Pygame Arcade</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #070e1b;
      --card-bg: rgba(15, 27, 49, 0.75);
      --card-border: rgba(56, 189, 248, 0.2);
      --primary: #38bdf8;
      --primary-hover: #0ea5e9;
      --accent: #fbbf24;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --code-bg: #020617;
      --border-radius: 16px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.6;
      background-image: 
        radial-gradient(circle at 15% 20%, rgba(56, 189, 248, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 85% 75%, rgba(251, 191, 36, 0.08) 0%, transparent 40%);
      background-attachment: fixed;
      padding: 2.5rem 1rem;
    }

    .container {
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 2rem;
    }

    header {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--border-radius);
      padding: 2.5rem;
      backdrop-filter: blur(12px);
      text-align: center;
      position: relative;
      overflow: hidden;
    }

    .badge-wrapper {
      display: flex;
      justify-content: center;
      gap: 0.6rem;
      flex-wrap: wrap;
      margin-bottom: 1.25rem;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      padding: 0.35rem 0.85rem;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      border-radius: 9999px;
      background: rgba(56, 189, 248, 0.12);
      color: var(--primary);
      border: 1px solid rgba(56, 189, 248, 0.3);
    }

    .badge.gold {
      background: rgba(251, 191, 36, 0.12);
      color: var(--accent);
      border-color: rgba(251, 191, 36, 0.3);
    }

    h1 {
      font-size: clamp(2rem, 5vw, 2.75rem);
      font-weight: 800;
      color: #fff;
      margin-bottom: 0.8rem;
      letter-spacing: -0.02em;
    }

    .subtitle {
      font-size: 1.15rem;
      color: var(--text-muted);
      max-width: 680px;
      margin: 0 auto 1.75rem auto;
    }

    .header-links {
      display: flex;
      justify-content: center;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.75rem 1.4rem;
      font-size: 0.95rem;
      font-weight: 600;
      border-radius: 10px;
      text-decoration: none;
      transition: all 0.2s ease;
      cursor: pointer;
    }

    .btn-primary {
      background: var(--primary);
      color: #031326;
    }

    .btn-primary:hover {
      background: var(--primary-hover);
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(56, 189, 248, 0.3);
    }

    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--border-radius);
      padding: 2rem;
      backdrop-filter: blur(12px);
    }

    h2 {
      font-size: 1.4rem;
      font-weight: 700;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      color: #fff;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 0.6rem;
    }

    .grid-2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.25rem;
    }

    .feature-item {
      background: rgba(2, 6, 23, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 12px;
      padding: 1.25rem;
    }

    .feature-item h3 {
      font-size: 1.05rem;
      color: var(--primary);
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .feature-item p {
      font-size: 0.9rem;
      color: var(--text-muted);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 0.5rem;
      font-size: 0.95rem;
    }

    th, td {
      padding: 0.85rem 1rem;
      text-align: left;
      border-bottom: 1px solid rgba(255, 255, 255, 0.07);
    }

    th {
      background: rgba(2, 6, 23, 0.6);
      color: var(--primary);
      font-weight: 700;
      text-transform: uppercase;
      font-size: 0.8rem;
      letter-spacing: 0.05em;
    }

    td kbd {
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 5px;
      padding: 0.2rem 0.5rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      color: #fff;
    }

    .code-block {
      background: var(--code-bg);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 1rem 1.25rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.88rem;
      color: #e2e8f0;
      overflow-x: auto;
      margin: 0.75rem 0 1.25rem 0;
    }

    .code-block code {
      display: block;
      line-height: 1.6;
    }

    .comment {
      color: #64748b;
    }

    footer {
      text-align: center;
      color: var(--text-muted);
      font-size: 0.85rem;
      margin-top: 1rem;
      padding-bottom: 2rem;
    }
  </style>
</head>
<body>

  <div class="container">
    <header>
      <div class="badge-wrapper">
        <span class="badge">Python 3.10+</span>
        <span class="badge">Pygame 2.5+</span>
        <span class="badge gold">Sem Assets Externos</span>
        <span class="badge">Áudio Procedural</span>
      </div>
      <h1>Argolas Aquáticas</h1>
      <p class="subtitle">
        Uma recriação nostálgica do brinquedo aquático dos anos 90 desenvolvida com física de fluidos e síntese matemática de áudio em tempo real.
      </p>
      <div class="header-links">
        <a href="https://github.com/Edinaldo-long/argolas-aquaticas" target="_blank" class="btn btn-primary">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
          Ver Código no GitHub
        </a>
      </div>
    </header>

    <section class="card">
      <h2>⚙️ Destaques Técnicos</h2>
      <div class="grid-2">
        <div class="feature-item">
          <h3>🌊 Física Hidrodinâmica</h3>
          <p>Cálculo em tempo real de arrasto vetorial, flutuabilidade, amortecimento em colisões e efeito venturi centralizado nos jatos de bolhas.</p>
        </div>
        <div class="feature-item">
          <h3>🔊 Síntese Procedural de Áudio</h3>
          <p>Efeitos sonoros (bloops, jatos d'água, cliques e fanfarras) gerados diretamente via ondas senoidais e arrays de memória sem nenhum arquivo WAV/MP3.</p>
        </div>
        <div class="feature-item">
          <h3>🎨 Renderização Primitiva Pura</h3>
          <p>Toda a arte, reflexos no vidro, deformação elíptica das argolas 3D e peixes em movimento são desenhados por matrizes matemáticas.</p>
        </div>
        <div class="feature-item">
          <h3>🏆 Mecânicas de Arcade</h3>
          <p>Sistema dinâmico de combos x5 com contador regressivo, argola dourada de tripla pontuação e salvamento automático de recorde local.</p>
        </div>
      </div>
    </section>

    <section class="card">
      <h2>🎮 Controles</h2>
      <table>
        <thead>
          <tr>
            <th>Ação</th>
            <th>Teclado</th>
            <th>Mouse</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Jato Esquerdo</strong></td>
            <td><kbd>Seta Esquerda</kbd> ou <kbd>Z</kbd></td>
            <td>Botão azul na tela</td>
          </tr>
          <tr>
            <td><strong>Jato Direito</strong></td>
            <td><kbd>Seta Direita</kbd> ou <kbd>M</kbd></td>
            <td>Botão vermelho na tela</td>
          </tr>
          <tr>
            <td><strong>Jato Duplo</strong></td>
            <td><kbd>Barra de Espaço</kbd></td>
            <td>Ambos os botões</td>
          </tr>
          <tr>
            <td><strong>Pausar</strong></td>
            <td><kbd>P</kbd></td>
            <td>—</td>
          </tr>
          <tr>
            <td><strong>Reiniciar / Novo Jogo</strong></td>
            <td><kbd>R</kbd></td>
            <td>Clique na tela</td>
          </tr>
        </tbody>
      </table>
    </section>

    <section class="card">
      <h2>🚀 Como Executar Localmente</h2>
      <p style="color: var(--text-muted); margin-bottom: 0.5rem; font-size: 0.95rem;">
        Clone o repositório e execute com Python instalado:
      </p>
      <div class="code-block">
        <code><span class="comment"># 1. Clonar o repositório</span><br>git clone https://github.com/Edinaldo-long/argolas-aquaticas.git<br>cd argolas-aquaticas<br><br><span class="comment"># 2. Instalar dependências</span><br>pip install pygame<br><br><span class="comment"># 3. Iniciar o jogo</span><br>python argolas_aquaticas.py</code>
      </div>
    </section>

    <footer>
      Desenvolvido por <strong>Edinaldo Santos de Almeida</strong> • Projeto para Portfólio de Desenvolvimento
    </footer>
  </div>

</body>
</html>
Como publicar como site no GitHub Pages:
Salve esse arquivo como index.html na pasta do seu projeto (C:\Users\esata\argolas_aquaticas).

Faça o envio para o GitHub:

PowerShell
git add index.html
git commit -m "docs: adicionar pagina web de apresentacao do jogo"
git push
No GitHub, entre em Settings > Pages e em Branch selecione main e / (root). Em poucos minutos, a página estará no ar pelo link [https://Edinaldo-long.github.io/argolas-aquaticas/](https://Edinaldo-long.github.io/argolas-aquaticas/)!

quero por esse projeto no git hub também

Instalar dependências:

Bash
pip install -r requirements.txt
Iniciar o jogo:

Bash
python pinball.py
🛠️ Tecnologias Utilizadas
Linguagem: Python

Biblioteca Gráfica/Áudio: Pygame

Módulos Nativos: math, random, array, sys, os

📄 Licença
Distribuído sob a licença MIT. Consulte o ficheiro LICENSE para mais detalhes.
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_pinball)

print("README.md gerado com sucesso.")


```text?code_stdout&code_event_index=1
README.md gerado com sucesso.

O jogo Pinball Neon tem um apelo técnico excelente para portfólio, sobretudo pela implementação de física própria com sub-stepping contínuo (para evitar efeito de tunneling em velocidades elevadas), cinemática rotacional dos flippers e síntese procedural de áudio.   
PY
+ 4

Abaixo encontra o passo a passo completo, juntamente com a documentação em Markdown e em HTML.

1. Criar o Novo Repositório no GitHub
Aceda a github.com/new e preencha:   
PNG

Repository name: pinball-neon (ou neon-pinball)

Description: Mesa clássica de arcade em estilo neon retro desenvolvida em Python/Pygame com simulação física de sub-stepping, cinemática de flippers e áudio procedural.

   
PY

Visibility: Public

   
PNG

Initialize this repository with: Mantenha as opções desmarcadas para subir direto da sua máquina sem conflitos.

Clique em Create repository.

2. Estrutura de Ficheiros na sua Máquina
Crie uma pasta dedicada (ex: C:\Users\esata\pinball_neon ou dentro da sua pasta de projetos) com os seguintes ficheiros:

Plaintext
pinball-neon/
│
├── pinball.py            # Código do jogo
├── requirements.txt      # Dependências
├── .gitignore            # Ignorar ficheiros temporários e o recorde local
├── README.md             # Documentação principal para o GitHub
└── index.html            # Página web do projeto (para GitHub Pages)
Ficheiro .gitignore:
Plaintext
__pycache__/
*.py[cod]
.venv/
venv/
pinball_recorde.txt
.vscode/
.idea/
Ficheiro requirements.txt:
Plaintext
pygame>=2.5.0
3. Ficheiros Gerados para Download e Uso
Os ficheiros completos para este projeto já foram gerados:

README para o GitHub: 
Ícone de MD
README
 MD 

Página Web Completa (HTML/CSS): 
Ícone de HTML
index_pinball
 HTML 

4. Código HTML Completo (index.html)
Caso queira copiar e colar diretamente no editor:

HTML
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Neon Pinball - Pygame Arcade</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #090714;
      --card-bg: rgba(22, 16, 46, 0.75);
      --card-border: rgba(192, 132, 252, 0.25);
      --primary: #c084fc;
      --primary-hover: #a855f7;
      --accent: #f43f5e;
      --accent-neon: #38bdf8;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --code-bg: #04020a;
      --border-radius: 16px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.6;
      background-image: 
        radial-gradient(circle at 20% 15%, rgba(192, 132, 252, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 80% 80%, rgba(244, 63, 94, 0.12) 0%, transparent 45%);
      background-attachment: fixed;
      padding: 2.5rem 1rem;
    }

    .container {
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 2rem;
    }

    header {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--border-radius);
      padding: 2.5rem;
      backdrop-filter: blur(12px);
      text-align: center;
      position: relative;
    }

    .badge-wrapper {
      display: flex;
      justify-content: center;
      gap: 0.6rem;
      flex-wrap: wrap;
      margin-bottom: 1.25rem;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      padding: 0.35rem 0.85rem;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      border-radius: 9999px;
      background: rgba(192, 132, 252, 0.12);
      color: var(--primary);
      border: 1px solid rgba(192, 132, 252, 0.35);
    }

    .badge.accent {
      background: rgba(244, 63, 94, 0.12);
      color: var(--accent);
      border-color: rgba(244, 63, 94, 0.35);
    }

    .badge.neon {
      background: rgba(56, 189, 248, 0.12);
      color: var(--accent-neon);
      border-color: rgba(56, 189, 248, 0.35);
    }

    h1 {
      font-size: clamp(2rem, 5vw, 2.75rem);
      font-weight: 800;
      color: #fff;
      margin-bottom: 0.8rem;
      letter-spacing: -0.02em;
      text-shadow: 0 0 20px rgba(192, 132, 252, 0.4);
    }

    .subtitle {
      font-size: 1.15rem;
      color: var(--text-muted);
      max-width: 680px;
      margin: 0 auto 1.75rem auto;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.75rem 1.4rem;
      font-size: 0.95rem;
      font-weight: 600;
      border-radius: 10px;
      text-decoration: none;
      transition: all 0.2s ease;
      cursor: pointer;
      background: var(--primary);
      color: #0b0717;
    }

    .btn:hover {
      background: var(--primary-hover);
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(168, 85, 247, 0.4);
    }

    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--border-radius);
      padding: 2rem;
      backdrop-filter: blur(12px);
    }

    h2 {
      font-size: 1.4rem;
      font-weight: 700;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      color: #fff;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 0.6rem;
    }

    .grid-2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.25rem;
    }

    .feature-item {
      background: rgba(4, 2, 10, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 12px;
      padding: 1.25rem;
    }

    .feature-item h3 {
      font-size: 1.05rem;
      color: var(--primary);
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .feature-item p {
      font-size: 0.9rem;
      color: var(--text-muted);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 0.5rem;
      font-size: 0.95rem;
    }

    th, td {
      padding: 0.85rem 1rem;
      text-align: left;
      border-bottom: 1px solid rgba(255, 255, 255, 0.07);
    }

    th {
      background: rgba(4, 2, 10, 0.6);
      color: var(--primary);
      font-weight: 700;
      text-transform: uppercase;
      font-size: 0.8rem;
      letter-spacing: 0.05em;
    }

    td kbd {
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 5px;
      padding: 0.2rem 0.5rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      color: #fff;
    }

    .code-block {
      background: var(--code-bg);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 1rem 1.25rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.88rem;
      color: #e2e8f0;
      overflow-x: auto;
      margin: 0.75rem 0 1.25rem 0;
    }

    .code-block code {
      display: block;
      line-height: 1.6;
    }

    .comment { color: #64748b; }

    footer {
      text-align: center;
      color: var(--text-muted);
      font-size: 0.85rem;
      margin-top: 1rem;
      padding-bottom: 2rem;
    }
  </style>
</head>
<body>

  <div class="container">
    <header>
      <div class="badge-wrapper">
        <span class="badge">Python 3.10+</span>
        <span class="badge">Pygame 2.5+</span>
        <span class="badge accent">Sub-stepping Físico</span>
        <span class="badge neon">Síntese Procedural</span>
      </div>
      <h1>⚡ Neon Pinball</h1>
      <p class="subtitle">
        Uma mesa clássica de arcade em estilo neon retro construída com motor físico personalizado, deteção contínua de colisões e efeitos sonoros gerados por código.
      </p>
      <div>
        <a href="https://github.com/Edinaldo-long/pinball-neon" target="_blank" class="btn">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
          Ver Código no GitHub
        </a>
      </div>
    </header>

    <section class="card">
      <h2>⚙️ Engenharia e Físicas do Jogo</h2>
      <div class="grid-2">
        <div class="feature-item">
          <h3>📐 Motor Físico com Sub-stepping</h3>
          <p>Iteração a 6 sub-passos por fotograma (360 Hz de resolução interna) para evitar efeito de *tunneling* em bolas a alta velocidade.</p>
        </div>
        <div class="feature-item">
          <h3>🕹️ Flippers com Cinemática Angular</h3>
          <p>Cálculo exato da velocidade angular instantânea transmitida tangencialmente para a bola durante a rotação mecânica.</p>
        </div>
        <div class="feature-item">
          <h3>💥 Mecânica de Multibola e Combos</h3>
          <p>Ao ativar todos os 5 alvos de topo, a mesa liberta esferas adicionais em simultâneo com deteção elástica de colisão bola-contra-bola.</p>
        </div>
        <div class="feature-item">
          <h3>🎶 Áudio por Síntese Matemática</h3>
          <p>Ondas senoidais, quadradas e ruído percussivo gerados diretamente no buffer do Pygame Mixer sem necessidade de ficheiros de áudio.</p>
        </div>
      </div>
    </section>

    <section class="card">
      <h2>🎮 Controlos da Mesa</h2>
      <table>
        <thead>
          <tr>
            <th>Ação</th>
            <th>Teclado</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Flipper Esquerdo</strong></td>
            <td><kbd>Seta Esquerda</kbd> ou <kbd>Z</kbd></td>
          </tr>
          <tr>
            <td><strong>Flipper Direito</strong></td>
            <td><kbd>Seta Direita</kbd> ou <kbd>M</kbd></td>
          </tr>
          <tr>
            <td><strong>Lançador (Plunger)</strong></td>
            <td><kbd>Barra de Espaço</kbd> (segurar para carregar, soltar para disparar)</td>
          </tr>
          <tr>
            <td><strong>Sacudir Mesa (Nudge)</strong></td>
            <td><kbd>Seta para Cima</kbd> ou <kbd>X</kbd> (máx. 3 vezes por bola)</td>
          </tr>
          <tr>
            <td><strong>Reiniciar Partida</strong></td>
            <td><kbd>R</kbd> (após o fim de jogo)</td>
          </tr>
          <tr>
            <td><strong>Sair</strong></td>
            <td><kbd>ESC</kbd></td>
          </tr>
        </tbody>
      </table>
    </section>

    <section class="card">
      <h2>🚀 Como Executar</h2>
      <div class="code-block">
        <code><span class="comment"># Clonar o repositório</span><br>git clone https://github.com/Edinaldo-long/pinball-neon.git<br>cd pinball-neon<br><br><span class="comment"># Instalar o Pygame</span><br>pip install pygame<br><br><span class="comment"># Executar o jogo</span><br>python pinball.py</code>
      </div>
    </section>

    <footer>
      Desenvolvido por <strong>Edinaldo Santos de Almeida</strong> • Portfólio de Engenharia de Software
    </footer>
  </div>

</body>
</html>
5. Enviar para o GitHub via Terminal
No PowerShell, dentro da pasta do projeto:

PowerShell
git init
git add .
git commit -m "feat: adicionar jogo Pinball Neon, documentacao e pagina web"
git branch -M main
git remote add origin https://github.com/Edinaldo-long/pinball-neon.git
git push -u origin main
https://github.com/Edinaldo-long/pinball.git

Para subir o jogo diretamente para o repositório [https://github.com/Edinaldo-long/pinball.git](https://github.com/Edinaldo-long/pinball.git), siga os passos abaixo:

Passo 1: Organizar a pasta local
Certifique-se de que a pasta onde está o ficheiro pinball.py contém também os ficheiros auxiliares:   
PY

pinball.py

   
PY

requirements.txt

.gitignore (para não rastrear ficheiros temporários nem o pinball_recorde.txt)   
PY

README.md (o ficheiro gerado anteriormente)   
MD

index.html (opcional, para criar a página de apresentação)   
HTML

(Caso ainda não tenha criado o .gitignore nessa pasta, crie um ficheiro de texto com o nome .gitignore contendo pinball_recorde.txt e __pycache__/).   
PY

Passo 2: Executar os comandos no terminal
Abra o terminal (PowerShell) dentro da pasta onde se encontram os ficheiros e execute a seguinte sequência:

PowerShell
# 1. Inicializar o repositório Git local
git init

# 2. Adicionar todos os ficheiros da pasta
git add .

# 3. Criar o primeiro commit
git commit -m "feat: versao inicial do Pinball Neon com fisica customizada e audio procedural"

# 4. Definir a branch principal como main
git branch -M main

# 5. Associar ao seu repositório remoto
git remote add origin https://github.com/Edinaldo-long/pinball.git

# 6. Enviar os ficheiros para o GitHub
git push -u origin main
Se o repositório já tiver sido criado com ficheiros (como README ou Licença no GitHub):
Se o comando git push apresentar um erro de rejeição (non-fast-forward), faça primeiro um pull antes do push:

PowerShell
git pull origin main --allow-unrelated-histories
git push -u origin main
Após concluir o envio, aceda a [https://github.com/Edinaldo-long/pinball](https://github.com/Edinaldo-long/pinball) no navegador para verificar a documentação e os ficheiros publicados.

Counting objects: 100% (4/4), done.

Delta compression using up to 4 threads

Compressing objects: 100% (3/3), done.

Writing objects: 100% (4/4), 6.61 KiB | 1.65 MiB/s, done.

Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)

To https://github.com/Edinaldo-long/pinball.git

 * [new branch]      main -> main

branch 'main' set up to track 'origin/main'.

PS C:\Users\esata\Pinball> 

O repositório do Pinball foi publicado com sucesso na ramificação main do GitHub!

Verificação e Próximos Passos Recomendados
Confirmar a publicação:

Abra no navegador o endereço [https://github.com/Edinaldo-long/pinball](https://github.com/Edinaldo-long/pinball) para visualizar o ficheiro README.md formatado na página inicial.   
MD

Ativar o GitHub Pages (Opcional):

Caso tenha colocado o ficheiro index.html na raiz do projeto:   
HTML

Aceda a Settings > Pages no repositório.

Na secção Build and deployment > Branch, escolha main e / (root).

Clique em Save. A página ficará acessível em:

[https://edinaldo-long.github.io/pinball/](https://edinaldo-long.github.io/pinball/)

Destacar no perfil (Pinned Repositories):

Vá até à página principal do seu perfil ([https://github.com/Edinaldo-long](https://github.com/Edinaldo-long)).

Clique em Customize your pins.

Selecione os repositórios argolas-aquaticas e pinball para que fiquem no topo da página de apresentação do seu portfólio.

quero por essa imagem no portfolio do git hub

Para incluir esta imagem no topo do README.md (e no site index.html) do repositório pinball, siga este passo a passo:

Passo 1: Salvar a imagem no projeto
Na pasta do seu projeto (C:\Users\esata\Pinball), crie uma subpasta chamada screenshots.

Salve a imagem enviada dentro dessa pasta com o nome exato:

gameplay.png (ficando o caminho: C:\Users\esata\Pinball\screenshots\gameplay.png).

Passo 2: Inserir a imagem no README.md
Abra o seu ficheiro README.md e adicione a linha da imagem logo abaixo do título e da descrição inicial:

Markdown
# ⚡ Neon Pinball (Pinball Neon)

Um jogo clássico de Pinball estilo retro-arcade/neon desenvolvido em Python e Pygame...

<p align="center">
  <img src="screenshots/gameplay.png" alt="Demonstração do Pinball Neon" width="420"/>
</p>

---
(Usar a tag <p align="center"><img ... width="420"/></p> mantém a captura de tela centralizada e com um tamanho proporcional no GitHub, sem esticar a visualização).

Passo 3: Inserir a imagem no index.html (Opcional, para o GitHub Pages)
Se estiver a utilizar a página web index.html, insira a imagem no cabeçalho ou logo após a descrição principal:

HTML
<div style="text-align: center; margin: 2rem 0;">
  <img src="screenshots/gameplay.png" alt="Demonstração do Pinball Neon" style="max-width: 380px; width: 100%; border-radius: 12px; border: 1px solid rgba(192, 132, 252, 0.3); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);">
</div>
Passo 4: Enviar a imagem e as alterações para o GitHub
No PowerShell dentro de C:\Users\esata\Pinball, execute:

PowerShell
git add .
git commit -m "docs: adicionar screenshot da gameplay no README"
git push
Ao recarregar a página [https://github.com/Edinaldo-long/pinball](https://github.com/Edinaldo-long/pinball), a captura da mesa neon surgirá imediatamente centralizada no topo da documentação.

me da a imagem pronta para eu colocar na pasta scrrenshots por favor

https://lh3.googleusercontent.com/gg/AJWXcNfK8qlhhgB17rUECvkEaqLUOvrh6CIY39b1-4MA0QF0p_76U-6MX9MbG-L2CR7LFcJbDNaYt4d6dOBDUyFu_9rlqn4nbGqQSPVmnqtudSPBvTBVeRSHAEkar5HCa1CHN45nLB_5tmFclvcatC4e7hylhRQ34kIVgZqwKpR4_2U2rpHOywsKPUCCnDZg1lj3_Reer57ipC-zouBEwvfXeJxRiyyNpfHGkD3Y8nBlUg4nMStmW60KVGv-Cr_j837vm50NnpB3YZne94grVG0RjjCKo2r5fYvX2nlEuVVDywkaTP9gw5OzjxUkUi39UA6SkA3rp68tuCrGdDEi2lcY4kk=s1600
Aqui está o ficheiro de imagem pronto para descarregar e utilizar:

Descarregar imagem pronta: [file-tag: code-generated-file-e047ca8a-efad-4a11-b016-d35d94943714]

Como guardar e enviar:
Descarregue o ficheiro acima ou clique com o botão direito sobre a imagem apresentada e selecione "Guardar imagem como...".

Guarde-a com o nome gameplay.png na pasta:

Plaintext
C:\Users\esata\Pinball\screenshots\gameplay.png
(se a pasta screenshots ainda não existir, crie-a dentro de C:\Users\esata\Pinball).

No seu terminal PowerShell em C:\Users\esata\Pinball, execute:

PowerShell
git add .
git commit -m "docs: adicionar screenshot da gameplay"
git push
A imagem ficará imediatamente visível no cabeçalho do seu repositório no GitHub!

faz um read me interessante por favor

Aqui está um README.md completo, moderno e altamente profissional para o repositório do Pinball, formatado com badges, apresentação visual centralizada, tabelas organizadas e detalhamento da arquitetura técnica (sub-stepping, colisões vetoriais e áudio por software).

Markdown
<div align="center">

# ⚡ Neon Pinball (Pinball Neon)

**Uma rec
faz um read me por favor de deixar o queixo caido

🔥 Multibola: Ao acender os 5 alvos de topo, o multiplicador de pontuação aumenta (até x5) e uma nova bola entra imediatamente em jogo pelo topo do ecrã!

🚀 Como Executar
Pré-requisitos
Python 3.10 ou superior instalado no sistema.

Passo a Passo
Clonar o repositório:

Bash
git clone [https://github.com/Edinaldo-long/pinball.git](https://github.com/Edinaldo-long/pinball.git)
cd pinball
Instalar a dependência:

Bash
pip install pygame
Executar a mesa:

Bash
python pinball.py
📁 Estrutura do Repositório
Plaintext
pinball/
│
├── pinball.py           # Código fonte completo do motor físico e renderização
├── requirements.txt     # Dependências mínimas (pygame)
├── .gitignore           # Exclusão de cache e recorde local
├── LICENSE              # Licença MIT
├── README.md            # Documentação técnica de apresentação
└── screenshots/
    └── gameplay.png     # Captura de ecrã da mesa em execução
👤 Autor
Desenvolvido por Edinaldo Santos de Almeida

with open("README_NEON.md", "w", encoding="utf-8") as f:
f.write(readme_neon)

print("README_NEON.md gerado.")


```text?code_stdout&code_event_index=1
README_NEON.md gerado.

Aqui está uma versão do README.md concebida com padrão de engenharia de software e computação gráfica. O texto valoriza as decisões técnicas de projeto (resolução de colisões a 360 Hz, cinemática rotacional vetorial, síntese DSP por software e independência de ficheiros externos), com badges dinâmicos e enquadramento visual da captura de ecrã.   
PY
+ 2

O ficheiro completo para descarregar:

Ficheiro README: 
Ícone de MD
README_NEON
 MD 

Conteúdo Completo para copiar para o README.md:
Markdown
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
  <img src="screenshots/gameplay.png" alt="Demonstração da Mesa Neon Pinball" width="380" style="border-radius: 14px; box-shadow: 0 10px 40px rgba(192, 132, 252, 0.35); border: 2px solid rgba(192, 132, 252, 0.4);"/>
</p>

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
🔥 Multibola: Ao acender os 5 alvos de topo, o multiplicador de pontuação aumenta (até x5) e uma nova bola entra imediatamente em jogo pelo topo do ecrã[cite: 5]!

🚀 Como Executar
Pré-requisitos
Python 3.10 ou superior instalado no sistema.

Passo a Passo
Clonar o repositório:

Bash
git clone [https://github.com/Edinaldo-long/pinball.git](https://github.com/Edinaldo-long/pinball.git)
cd pinball
Instalar a dependência:

Bash
pip install pygame
Executar a mesa:

Bash
python pinball.py
📁 Estrutura do Repositório
Plaintext
pinball/
│
├── pinball.py           # Código fonte completo do motor físico e renderização
├── requirements.txt     # Dependências mínimas (pygame)
├── .gitignore           # Exclusão de cache e recorde local
├── LICENSE              # Licença MIT
├── README.md            # Documentação técnica de apresentação
└── screenshots/
    └── gameplay.png     # Captura de ecrã da mesa em execução
👤 Autor
Desenvolvido por Edinaldo Santos de Almeida

Como aplicar a alteração:
Abra o ficheiro README.md na pasta C:\Users\esata\Pinball.

Substitua o conteúdo pelo texto acima e guarde o ficheiro.

Certifique-se de que o ficheiro gameplay.png está na pasta screenshots/[cite: 9].

No terminal, envie a atualização:

PowerShell
git add README.md screenshots/gameplay.png
git commit -m "docs: reformulacao profissional do README com analise tecnica"
git push
nao apareceu a imagem

O ficheiro gameplay.png já está guardado no sítio certo (EDINALDO ALMEIDA > Pinball > screenshots). O motivo pelo qual a imagem ainda não apareceu no GitHub é porque ela ainda não foi enviada para o repositório remoto através do Git (ou o ficheiro foi guardado apenas localmente após o último git push).   
PNG

Como resolver pelo terminal
Abra o terminal (PowerShell ou Git Bash) na pasta Pinball e execute os seguintes comandos:

PowerShell
git status
(Deverá ver a pasta screenshots/ ou o ficheiro screenshots/gameplay.png listado a vermelho como ficheiro por rastrear).

Em seguida, adicione e envie a imagem:

PowerShell
git add screenshots/gameplay.png README.md
git commit -m "docs: adicionar imagem de gameplay e atualizar README"
git push origin main
Verificação no README
Certifique-se de que a linha de inclusão da imagem no seu README.md está exatamente assim (sem barras invertidas \ nem caminhos absolutos do Windows):   
MD

Markdown
<p align="center">
  <img src="screenshots/gameplay.png" alt="Demonstração da Mesa Neon Pinball" width="380"/>
</p>
ou em formato Markdown simples:   
MD

Markdown
![Demonstração da Mesa Neon Pinball](screenshots/gameplay.png)
Depois de executar o git push, atualize a página do repositório no navegador com Ctrl + F5 para limpar a cache do navegador e a imagem surgirá no topo do projeto.

Untracked files:

  (use "git add <file>..." to include in what will be committed)

        screenshots/



nothing added to commit but untracked files present (use "git add" to track)

PS C:\Users\esata\Pinball> 

Exatamente isso: a pasta screenshots/ ainda estava marcada como não rastreada (untracked). Por essa razão, a imagem ainda não tinha sido enviada para o GitHub.

Execute os seguintes comandos no seu terminal para adicionar a pasta e enviar a imagem:

PowerShell
git add screenshots/
git commit -m "docs: adicionar screenshot da gameplay"
git push origin main
Após a conclusão do envio, aceda à página do repositório no navegador ([https://github.com/Edinaldo-long/pinball](https://github.com/Edinaldo-long/pinball)) e prima Ctrl + F5 para atualizar a página. A captura da mesa neon aparecerá imediatamente no cabeçalho do projeto.

estou usando esse codigo e a imagem na aparece

Se a pasta screenshots/ já foi enviada no GitHub mas a imagem continua sem renderizar, o motivo costuma ser um destes 3 pontos:

1. Tag HTML <img> com fechamento ou caminho sensível a maiúsculas
O GitHub Flavored Markdown é estritamente case-sensitive (diferencia maiúsculas de minúsculas). Verifique se o nome do arquivo na pasta é exatamente minúsculo (gameplay.png).

Experimente substituir a tag <img> pelo formato padrão nativo do Markdown, ou simplificar o HTML:

Opção A (Markdown puro — mais compatível):
Markdown
![Demonstração da Mesa Neon Pinball](screenshots/gameplay.png)
Opção B (HTML centralizado simples sem estilos extras):
HTML
<p align="center">
  <img src="./screenshots/gameplay.png" alt="Demonstração" width="380">
</p>
2. O arquivo gameplay.png foi comitado e enviado de fato?
Para ter 100% de certeza se o arquivo está na nuvem do GitHub:

Abra o terminal no VS Code / PowerShell dentro de C:\Users\esata\Pinball.

Rode:

PowerShell
git status
Se aparecer nothing to commit, working tree clean, rode:

PowerShell
git push origin main
Acesse diretamente pelo navegador o endereço da imagem:
[https://github.com/Edinaldo-long/pinball/blob/main/screenshots/gameplay.png](https://github.com/Edinaldo-long/pinball/blob/main/screenshots/gameplay.png)

Se abrir uma página 404 (Not Found), significa que o push não enviou o arquivo gameplay.png.

Se abrir e mostrar a imagem perfeitamente, o problema é apenas a forma como o link foi escrito no README.md.

3. Usar a URL bruta direta (Raw) caso o caminho relativo falhe
Se mesmo com o arquivo no repositório o caminho relativo screenshots/gameplay.png não abrir, use o link direto absoluto do GitHub:

Markdown
<p align="center">
  <img src="https://raw.githubusercontent.com/Edinaldo-long/pinball/main/screenshots/gameplay.png" alt="Neon Pinball" width="380">
</p>
Para aplicar a correção agora:
Altere a linha da imagem no seu README.md para:

Markdown
<p align="center">
  <img src="https://raw.githubusercontent.com/Edinaldo-long/pinball/main/screenshots/gameplay.png" alt="Neon Pinball" width="380">
</p>
E no terminal execute:

PowerShell
git add README.md
git commit -m "fix: ajustar caminho da imagem no README"
git push origin main
estou usando esse codigo: <div align="center">



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

**Solução:** O ciclo principal divide cada fotograma em **6 sub-passos temporais discretos** (`SUBSTEPS = 6`), elevando a taxa de amostragem interna para **360 Hz**[cite: 5].
A integração das equações de Euler modificadas assegura trajetórias estáveis e colisões contínuas mesmo durante impactos elásticos de alta intensidade.


### 2. 🕹️ Cinemática Rotacional dos Flippers

Os batentes (flippers) não atuam apenas como defletores geométricos estáticos:

O sistema calcula a **velocidade angular instantânea** ($\omega = \frac{\Delta\theta}{\Delta t}$) da ponta e do corpo do flipper[cite: 5].
No momento do contacto, a velocidade superficial tangencial é calculada vetorialmente[cite: 5]:
  $$\vec{v}_{\text{superfície}} = (-\omega \cdot r_y, \; \omega \cdot r_x)$$

Essa velocidade é transferida diretamente como momento linear adicional para a bola, permitindo tacadas calculadas, amortecimentos suaves e disparos com base no tempo de acionamento[cite: 5].


### 3. 🔊 Síntese Procedural de Áudio (DSP por Software)

Nenhum ficheiro `.wav` ou `.mp3` é necessário no repositório. O jogo sintetiza som diretamente na memória RAM através do módulo nativo `array` do Python[cite: 5]:

**Bumpers & Plunger:** Modulação de frequência por chirp senoidal ($f_0 \to f_1$) combinada com decaimento exponencial de envelope ($e^{-kt}$)[cite: 5].
**Flippers & Slingshots:** Injeção controlada de ruído pseudo-aleatório (ruído branco filtrado) misturado com frequências graves para simular o solenoide mecânico[cite: 5].
**Alvos e Bónus:** Ondas quadradas harmónicas sintetizadas por software para timbres característicos de chips de som vintage[cite: 5].


### 4. 🧮 Geometria Analítica e Deteção Contínua

**Projeção Escalar em Segmentos:** Cálculo parametrizado $t \in [0, 1]$ para deteção precisa em paredes lineares e guias angulares[cite: 5].
**Colisão Elástica Esfera-contra-Esfera (Multibola):** Resolução de sobreposição geométrica com conservação de momento linear nos eixos normais de impacto[cite: 5].


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

O motivo pelo qual a imagem não aparece é exatamente porque a tag que chama a imagem foi apagada desse trecho do código!

Repare nesta parte do seu texto:

HTML
<br/>



<p align="center">
  <b>Uma mesa completa de Pinball retro-arcade...
Entre o <br/> e o <p align="center"><b>Uma mesa..., está um espaço em branco onde deveria estar a tag <img ... />.   
MD

Código com a correção inserida
Substitua o início do seu README.md exatamente por este bloco (repare na linha da imagem incluída):   
MD

Markdown
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
  <img src="screenshots/gameplay.png" alt="Demonstração da Mesa Neon Pinball" width="380"/>
</p>

<p align="center">
  <b>Uma mesa completa de Pinball retro-arcade com física de corpos rígidos vetorial implementada do zero em Python nativo, sem motores externos como Box2D ou Pymunk, e sem recurso a ficheiros de áudio ou sprites externos.</b>
</p>

[🎮 Controlos](#-controlos) • [🔬 Engenharia & Físicas](#-arquitetura-e-engenharia-de-física) • [🕹️ Regras da Mesa](#-regras-e-pontuação) • [🚀 Instalação](#-como-executar)

---

</div>
Se ainda assim não carregar no GitHub:
Confirme se o envio da pasta screenshots foi concluído:

No terminal na pasta do projeto, execute:

PowerShell
git add screenshots/ README.md
git commit -m "docs: adicionar imagem ao README"
git push origin main
Caso o caminho relativo falhe:

Substitua src="screenshots/gameplay.png" pela URL direta:

HTML
<img src="https://raw.githubusercontent.com/Edinaldo-long/pinball/main/screenshots/gameplay.png" alt="Demonstração" width="380"/>
me de o codigo na integra corrigido por favor

Vou gerar agora o arquivo README.md completo e 100% corrigido, contendo a tag de imagem configurada com link direto e seguro do GitHub para garantir a renderização imediata, além de todas as seções técnicas formatadas.

README.md
⚡ NEON PINBALL ARCADE
Simulação Física de Alta Fidelidade • Síntese de Áudio Procedural • Gráficos Vetoriais Puros
🎮 Controlos • 🔬 Engenharia & Físicas • 🕹️ Regras da Mesa • 🚀 Instalação

🌟 Visão Geral do Projeto
O Neon Pinball recria a dinâmica real de uma máquina eletromecânica de flippers dos anos 80/90. O diferencial deste projeto reside na sua independência de assets externos: todos os elementos visuais, curvaturas de rampa, colisores, partículas incandescentes e sons de impacto são calculados e gerados proceduralmente por código matemático em tempo de execução.

🔬 Arquitetura e Engenharia de Física
1. ⚙️ Pipeline Física com Sub-Stepping (Anti-Tunneling)
Bolas de pinball atingem velocidades de pico elevadas (MAX_SPEED = 27 px/frame). Em motores físicos a 60 FPS, isso causaria o efeito de tunneling (a bola atravessar paredes ou flippers entre fotogramas consecutivos).

Solução: O ciclo principal divide cada fotograma em 6 sub-passos temporais discretos (SUBSTEPS = 6), elevando a taxa de amostragem interna para 360 Hz.

A integração das equações de Euler modificadas assegura trajetórias estáveis e colisões contínuas mesmo durante impactos elásticos de alta intensidade.

2. 🕹️ Cinemática Rotacional dos Flippers
Os batentes (flippers) não atuam apenas como defletores geométricos estáticos:

O sistema calcula a velocidade angular instantânea (ω= 
Δt
Δθ
​
 ) da ponta e do corpo do flipper.

No momento do contacto, a velocidade superficial tangencial é calculada vetorialmente:


v
  
superf 
ı
ˊ
 cie
​
 =(−ω⋅r 
y
​
 ,ω⋅r 
x
​
 )
Essa velocidade é transferida diretamente como momento linear adicional para a bola, permitindo tacadas calculadas, amortecimentos suaves e disparos com base no tempo de acionamento.

3. 🔊 Síntese Procedural de Áudio (DSP por Software)
Nenhum ficheiro .wav ou .mp3 é necessário no repositório. O jogo sintetiza som diretamente na memória RAM através do módulo nativo array do Python:

Bumpers & Plunger: Modulação de frequência por chirp senoidal (f 
0
​
 →f 
1
​
 ) combinada com decaimento exponencial de envelope (e 
−kt
 ).

Flippers & Slingshots: Injeção controlada de ruído pseudo-aleatório (ruído branco filtrado) misturado com frequências graves para simular o solenoide mecânico.

Alvos e Bónus: Ondas quadradas harmónicas sintetizadas por software para timbres característicos de chips de som vintage.

4. 🧮 Geometria Analítica e Deteção Contínua
Projeção Escalar em Segmentos: Cálculo parametrizado t∈[0,1] para deteção precisa em paredes lineares e guias angulares.

Colisão Elástica Esfera-contra-Esfera (Multibola): Resolução de sobreposição geométrica com conservação de momento linear nos eixos normais de impacto.

🎮 Controlos
Comando

Tecla Teclado

Efeito Mecânico

Flipper Esquerdo

Seta Esquerda ou Z

Aciona o flipper esquerdo com rotação acelerada

Flipper Direito

Seta Direita ou M

Aciona o flipper direito com rotação acelerada

Mola de Lançamento

Barra de Espaço

Segure para tensionar a mola; solte para disparar

Sacudir Mesa (Nudge)

Seta para Cima ou X

Aplica aceleração caótica (máximo de 3 vezes por bola)

Reiniciar Partida

R

Reinicia a mesa após o ecrã de Fim de Jogo

Sair

ESC

Encerra a aplicação

🕹️ Regras e Pontuação
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

🔥 Multibola: Ao acender os 5 alvos de topo, o multiplicador de pontuação aumenta (até x5) e uma nova bola entra imediatamente em jogo pelo topo do ecrã!

🚀 Como Executar
Pré-requisitos
Python 3.10 ou superior instalado no sistema.

Passo a Passo
Clonar o repositório:

git clone https://github.com/Edinaldo-long/pinball.git
cd pinball

Instalar a dependência:

pip install pygame

Executar a mesa:

python pinball.py

📁 Estrutura do Repositório
pinball/
│
├── pinball.py           # Código fonte completo do motor físico e renderização
├── requirements.txt     # Dependências mínimas (pygame)
├── .gitignore           # Exclusão de cache e recorde local
├── LICENSE              # Licença MIT
├── README.md            # Documentação técnica de apresentação
└── screenshots/
    └── gameplay.png     # Captura de ecrã da mesa em execução

👤 Autor
Desenvolvido por Edinaldo Santos de Almeida

Edite diretamente ou com o Gemini
 Clique em qualquer lugar para escrever e editar diretamente ou selecione texto para pedir alterações ao Gemini. 
O arquivo acima foi gerado na íntegra com a tag de imagem configurada via URL bruta segura (raw.githubusercontent.com), que contorna eventuais falhas de resolução relativa do GitHub.

Para atualizar o repositório com este conteúdo:

Copie o conteúdo para o seu README.md na pasta Pinball.

No terminal (PowerShell), execute:

PowerShell
   git add README.md
   git commit -m "docs: corrigir caminho da imagem no README"
   git push origin main
preciso do codigo em html para copiar e colar diretamento no git hub

O seu ficheiro HTML está pronto para descarregar:

Ícone de HTML
README_FINAL
 HTML 
Aqui tem o código completo em HTML puro (compatível a 100% tanto para colar diretamente no editor do README.md do GitHub quanto num ficheiro index.html). A imagem está com a tag <img> configurada através do URL direto do seu repositório:

HTML
<div align="center">

  <h1>⚡ NEON PINBALL ARCADE</h1>
  <p><em>Simulação Física de Alta Fidelidade • Síntese de Áudio Procedural • Gráficos Vetoriais Puros</em></p>

  <p>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
    <a href="https://www.pygame.org/"><img src="https://img.shields.io/badge/Pygame-2.5+-FFE873?style=for-the-badge&logo=python&logoColor=3776AB" alt="Pygame 2.5+"></a>
    <a href="https://github.com/Edinaldo-long/pinball"><img src="https://img.shields.io/badge/Physics-Custom_Sub--Stepping-f43f5e?style=for-the-badge&logo=target" alt="Custom Sub-stepping Physics"></a>
    <a href="https://github.com/Edinaldo-long/pinball"><img src="https://img.shields.io/badge/Audio-Procedural_PCM-38bdf8?style=for-the-badge&logo=soundcloud" alt="Procedural PCM Audio"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-c084fc?style=for-the-badge" alt="MIT License"></a>
  </p>

  <br>

  <p align="center">
    <img src="https://raw.githubusercontent.com/Edinaldo-long/pinball/main/screenshots/gameplay.png" alt="Demonstração da Mesa Neon Pinball" width="380" style="border-radius: 14px; box-shadow: 0 10px 40px rgba(192, 132, 252, 0.35); border: 2px solid rgba(192, 132, 252, 0.4);">
  </p>

  <p align="center">
    <b>Uma mesa completa de Pinball retro-arcade com física de corpos rígidos vetorial implementada do zero em Python nativo, sem motores externos como Box2D ou Pymunk, e sem recurso a ficheiros de áudio ou sprites externos.</b>
  </p>

  <p>
    <a href="#-controlos">🎮 Controlos</a> •
    <a href="#-arquitetura-e-engenharia-de-física">🔬 Engenharia &amp; Físicas</a> •
    <a href="#-regras-e-pontuação">🕹️ Regras da Mesa</a> •
    <a href="#-como-executar">🚀 Instalação</a>
  </p>

  <hr>

</div>

<h2>🌟 Visão Geral do Projeto</h2>

<p>
  O <strong>Neon Pinball</strong> recria a dinâmica real de uma máquina eletromecânica de flippers dos anos 80/90. O diferencial deste projeto reside na sua <strong>independência de assets externos</strong>: todos os elementos visuais, curvaturas de rampa, colisores, partículas incandescentes e sons de impacto são calculados e gerados proceduralmente por código matemático em tempo de execução.
</p>

<hr>

<h2 id="-arquitetura-e-engenharia-de-física">🔬 Arquitetura e Engenharia de Física</h2>

<h3>1. ⚙️ Pipeline Física com Sub-Stepping (Anti-Tunneling)</h3>
<p>
  Bolas de pinball atingem velocidades de pico elevadas (<code>MAX_SPEED = 27 px/frame</code>). Em motores físicos a 60 FPS, isso causaria o efeito de <em>tunneling</em> (a bola atravessar paredes ou flippers entre fotogramas consecutivos).
</p>
<ul>
  <li><strong>Solução:</strong> O ciclo principal divide cada fotograma em <strong>6 sub-passos temporais discretos</strong> (<code>SUBSTEPS = 6</code>), elevando a taxa de amostragem interna para <strong>360 Hz</strong>.</li>
  <li>A integração das equações de Euler modificadas assegura trajetórias estáveis e colisões contínuas mesmo durante impactos elásticos de alta intensidade.</li>
</ul>

<h3>2. 🕹️ Cinemática Rotacional dos Flippers</h3>
<p>
  Os batentes (flippers) não atuam apenas como defletores geométricos estáticos:
</p>
<ul>
  <li>O sistema calcula a <strong>velocidade angular instantânea</strong> (<code>ω = Δθ / Δt</code>) da ponta e do corpo do flipper.</li>
  <li>No momento do contacto, a velocidade superficial tangencial é calculada vetorialmente: <code>v_superfície = (-ω · r_y, ω · r_x)</code>.</li>
  <li>Essa velocidade é transferida diretamente como momento linear adicional para a bola, permitindo tacadas calculadas, amortecimentos suaves e disparos com base no tempo de acionamento.</li>
</ul>

<h3>3. 🔊 Síntese Procedural de Áudio (DSP por Software)</h3>
<p>
  Nenhum ficheiro <code>.wav</code> ou <code>.mp3</code> é necessário no repositório. O jogo sintetiza som diretamente na memória RAM através do módulo nativo <code>array</code> do Python:
</p>
<ul>
  <li><strong>Bumpers &amp; Plunger:</strong> Modulação de frequência por chirp senoidal combinada com decaimento exponencial de envelope.</li>
  <li><strong>Flippers &amp; Slingshots:</strong> Injeção controlada de ruído pseudo-aleatório (ruído branco filtrado) misturado com frequências graves para simular o solenoide mecânico.</li>
  <li><strong>Alvos e Bónus:</strong> Ondas quadradas harmónicas sintetizadas por software para timbres característicos de chips de som vintage.</li>
</ul>

<h3>4. 🧮 Geometria Analítica e Deteção Contínua</h3>
<ul>
  <li><strong>Projeção Escalar em Segmentos:</strong> Cálculo parametrizado <code>t ∈ [0, 1]</code> para deteção precisa em paredes lineares e guias angulares.</li>
  <li><strong>Colisão Elástica Esfera-contra-Esfera (Multibola):</strong> Resolução de sobreposição geométrica com conservação de momento linear nos eixos normais de impacto.</li>
</ul>

<hr>

<h2 id="-controlos">🎮 Controlos</h2>

<table>
  <thead>
    <tr>
      <th align="left">Comando</th>
      <th align="left">Tecla Teclado</th>
      <th align="left">Efeito Mecânico</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Flipper Esquerdo</strong></td>
      <td><kbd>Seta Esquerda</kbd> ou <kbd>Z</kbd></td>
      <td>Aciona o flipper esquerdo com rotação acelerada</td>
    </tr>
    <tr>
      <td><strong>Flipper Direito</strong></td>
      <td><kbd>Seta Direita</kbd> ou <kbd>M</kbd></td>
      <td>Aciona o flipper direito com rotação acelerada</td>
    </tr>
    <tr>
      <td><strong>Mola de Lançamento</strong></td>
      <td><kbd>Barra de Espaço</kbd></td>
      <td><strong>Segure</strong> para tensionar a mola; <strong>solte</strong> para disparar</td>
    </tr>
    <tr>
      <td><strong>Sacudir Mesa (Nudge)</strong></td>
      <td><kbd>Seta para Cima</kbd> ou <kbd>X</kbd></td>
      <td>Aplica aceleração caótica (máximo de 3 vezes por bola)</td>
    </tr>
    <tr>
      <td><strong>Reiniciar Partida</strong></td>
      <td><kbd>R</kbd></td>
      <td>Reinicia a mesa após o ecrã de Fim de Jogo</td>
    </tr>
    <tr>
      <td><strong>Sair</strong></td>
      <td><kbd>ESC</kbd></td>
      <td>Encerra a aplicação</td>
    </tr>
  </tbody>
</table>

<hr>

<h2 id="-regras-e-pontuação">🕹️ Regras e Pontuação</h2>

<table>
  <thead>
    <tr>
      <th align="left">Elemento</th>
      <th align="left">Pontuação</th>
      <th align="left">Efeito Especial</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Bumpers Centrais</strong></td>
      <td>100 × Multiplicador</td>
      <td>Impulso elástico radial +4.5</td>
    </tr>
    <tr>
      <td><strong>Kickers / Slingshots</strong></td>
      <td>50 × Multiplicador</td>
      <td>Repulsão angular rápida</td>
    </tr>
    <tr>
      <td><strong>Alvos Superiores (5x)</strong></td>
      <td>500 × Multiplicador</td>
      <td>Ilumina indicador neon</td>
    </tr>
    <tr>
      <td><strong>Combo Todos os 5 Alvos</strong></td>
      <td>+2.500 Pontos</td>
      <td>Aumenta Multiplicador e ativa MULTIBOLA</td>
    </tr>
    <tr>
      <td><strong>Bola Extra</strong></td>
      <td>Atingir 20.000 pts</td>
      <td>+1 Vida adicional</td>
    </tr>
  </tbody>
</table>

<blockquote>
  <p><strong>🔥 Multibola:</strong> Ao acender os 5 alvos de topo, o multiplicador de pontuação aumenta (até <strong>x5</strong>) e uma nova bola entra imediatamente em jogo pelo topo do ecrã!</p>
</blockquote>

<hr>

<h2 id="-como-executar">🚀 Como Executar</h2>

<h3>Pré-requisitos</h3>
<ul>
  <li>Python 3.10 ou superior instalado.</li>
</ul>

<h3>Passo a Passo</h3>
<pre><code># 1. Clonar o repositório
git clone https://github.com/Edinaldo-long/pinball.git
cd pinball

# 2. Instalar a dependência
pip install pygame

# 3. Executar a mesa
python pinball.py</code></pre>

<hr>

<h2>📁 Estrutura do Repositório</h2>

<pre><code>pinball/
│
├── pinball.py           # Código fonte completo do motor físico e renderização
├── requirements.txt     # Dependências mínimas (pygame)
├── .gitignore           # Exclusão de cache e recorde local
├── LICENSE              # Licença MIT
├── README.md            # Documentação técnica de apresentação
└── screenshots/
    └── gameplay.png     # Captura de ecrã da mesa em execução</code></pre>

<hr>

<h2>👤 Autor</h2>

<p>
  Desenvolvido por <strong>Edinaldo Santos de Almeida</strong><br>
  <a href="https://github.com/Edinaldo-long"><img src="https://img.shields.io/badge/GitHub-Edinaldo--long-181717?style=flat-square&logo=github" alt="GitHub"></a>
</p>

<hr>

<div align="center">
  <sub>Licenciado sob a Licença MIT. Desenvolvido para fins de estudo de engenharia de jogos, física computacional e computação gráfica 2D.</sub>
</div>
Como aplicar diretamente pelo navegador no GitHub:
Aceda à página do seu repositório: [https://github.com/Edinaldo-long/pinball](https://github.com/Edinaldo-long/pinball).

Clique no ficheiro README.md e no ícone de lápis ✏️ (Edit this file).

Selecione todo o conteúdo existente e cole o código HTML acima.

Clique no botão verde Commit changes... no canto superior direito para guardar.





O Gemini é IA e pode cometer erros.

Analisando
<div align="center">

  <h1>⚡ NEON PINBALL ARCADE</h1>
  <p><em>Simulação Física de Alta Fidelidade • Síntese de Áudio Procedural • Gráficos Vetoriais Puros</em></p>

  <p>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
    <a href="https://www.pygame.org/"><img src="https://img.shields.io/badge/Pygame-2.5+-FFE873?style=for-the-badge&logo=python&logoColor=3776AB" alt="Pygame 2.5+"></a>
    <a href="https://github.com/Edinaldo-long/pinball"><img src="https://img.shields.io/badge/Physics-Custom_Sub--Stepping-f43f5e?style=for-the-badge&logo=target" alt="Custom Sub-stepping Physics"></a>
    <a href="https://github.com/Edinaldo-long/pinball"><img src="https://img.shields.io/badge/Audio-Procedural_PCM-38bdf8?style=for-the-badge&logo=soundcloud" alt="Procedural PCM Audio"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-c084fc?style=for-the-badge" alt="MIT License"></a>
  </p>

  <br>

  <p align="center">
    <img src="https://raw.githubusercontent.com/Edinaldo-long/pinball/main/screenshots/gameplay.png" alt="Demonstração da Mesa Neon Pinball" width="380" style="border-radius: 14px; box-shadow: 0 10px 40px rgba(192, 132, 252, 0.35); border: 2px solid rgba(192, 132, 252, 0.4);">
  </p>

  <p align="center">
    <b>Uma mesa completa de Pinball retro-arcade com física de corpos rígidos vetorial implementada do zero em Python nativo, sem motores externos como Box2D ou Pymunk, e sem recurso a ficheiros de áudio ou sprites externos.</b>
  </p>

  <p>
    <a href="#-controlos">🎮 Controlos</a> •
    <a href="#-arquitetura-e-engenharia-de-física">🔬 Engenharia &amp; Físicas</a> •
    <a href="#-regras-e-pontuação">🕹️ Regras da Mesa</a> •
    <a href="#-como-executar">🚀 Instalação</a>
  </p>

  <hr>

</div>

<h2>🌟 Visão Geral do Projeto</h2>

<p>
  O <strong>Neon Pinball</strong> recria a dinâmica real de uma máquina eletromecânica de flippers dos anos 80/90. O diferencial deste projeto reside na sua <strong>independência de assets externos</strong>: todos os elementos visuais, curvaturas de rampa, colisores, partículas incandescentes e sons de impacto são calculados e gerados proceduralmente por código matemático em tempo de execução.
</p>

<hr>

<h2 id="-arquitetura-e-engenharia-de-física">🔬 Arquitetura e Engenharia de Física</h2>

<h3>1. ⚙️ Pipeline Física com Sub-Stepping (Anti-Tunneling)</h3>
<p>
  Bolas de pinball atingem velocidades de pico elevadas (<code>MAX_SPEED = 27 px/frame</code>). Em motores físicos a 60 FPS, isso causaria o efeito de <em>tunneling</em> (a bola atravessar paredes ou flippers entre fotogramas consecutivos).
</p>
<ul>
  <li><strong>Solução:</strong> O ciclo principal divide cada fotograma em <strong>6 sub-passos temporais discretos</strong> (<code>SUBSTEPS = 6</code>), elevando a taxa de amostragem interna para <strong>360 Hz</strong>.</li>
  <li>A integração das equações de Euler modificadas assegura trajetórias estáveis e colisões contínuas mesmo durante impactos elásticos de alta intensidade.</li>
</ul>

<h3>2. 🕹️ Cinemática Rotacional dos Flippers</h3>
<p>
  Os batentes (flippers) não atuam apenas como defletores geométricos estáticos:
</p>
<ul>
  <li>O sistema calcula a <strong>velocidade angular instantânea</strong> (<code>ω = Δθ / Δt</code>) da ponta e do corpo do flipper.</li>
  <li>No momento do contacto, a velocidade superficial tangencial é calculada vetorialmente: <code>v_superfície = (-ω · r_y, ω · r_x)</code>.</li>
  <li>Essa velocidade é transferida diretamente como momento linear adicional para a bola, permitindo tacadas calculadas, amortecimentos suaves e disparos com base no tempo de acionamento.</li>
</ul>

<h3>3. 🔊 Síntese Procedural de Áudio (DSP por Software)</h3>
<p>
  Nenhum ficheiro <code>.wav</code> ou <code>.mp3</code> é necessário no repositório. O jogo sintetiza som diretamente na memória RAM através do módulo nativo <code>array</code> do Python:
</p>
<ul>
  <li><strong>Bumpers &amp; Plunger:</strong> Modulação de frequência por chirp senoidal combinada com decaimento exponencial de envelope.</li>
  <li><strong>Flippers &amp; Slingshots:</strong> Injeção controlada de ruído pseudo-aleatório (ruído branco filtrado) misturado com frequências graves para simular o solenoide mecânico.</li>
  <li><strong>Alvos e Bónus:</strong> Ondas quadradas harmónicas sintetizadas por software para timbres característicos de chips de som vintage.</li>
</ul>

<h3>4. 🧮 Geometria Analítica e Deteção Contínua</h3>
<ul>
  <li><strong>Projeção Escalar em Segmentos:</strong> Cálculo parametrizado <code>t ∈ [0, 1]</code> para deteção precisa em paredes lineares e guias angulares.</li>
  <li><strong>Colisão Elástica Esfera-contra-Esfera (Multibola):</strong> Resolução de sobreposição geométrica com conservação de momento linear nos eixos normais de impacto.</li>
</ul>

<hr>

<h2 id="-controlos">🎮 Controlos</h2>

<table>
  <thead>
    <tr>
      <th align="left">Comando</th>
      <th align="left">Tecla Teclado</th>
      <th align="left">Efeito Mecânico</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Flipper Esquerdo</strong></td>
      <td><kbd>Seta Esquerda</kbd> ou <kbd>Z</kbd></td>
      <td>Aciona o flipper esquerdo com rotação acelerada</td>
    </tr>
    <tr>
      <td><strong>Flipper Direito</strong></td>
      <td><kbd>Seta Direita</kbd> ou <kbd>M</kbd></td>
      <td>Aciona o flipper direito com rotação acelerada</td>
    </tr>
    <tr>
      <td><strong>Mola de Lançamento</strong></td>
      <td><kbd>Barra de Espaço</kbd></td>
      <td><strong>Segure</strong> para tensionar a mola; <strong>solte</strong> para disparar</td>
    </tr>
    <tr>
      <td><strong>Sacudir Mesa (Nudge)</strong></td>
      <td><kbd>Seta para Cima</kbd> ou <kbd>X</kbd></td>
      <td>Aplica aceleração caótica (máximo de 3 vezes por bola)</td>
    </tr>
    <tr>
      <td><strong>Reiniciar Partida</strong></td>
      <td><kbd>R</kbd></td>
      <td>Reinicia a mesa após o ecrã de Fim de Jogo</td>
    </tr>
    <tr>
      <td><strong>Sair</strong></td>
      <td><kbd>ESC</kbd></td>
      <td>Encerra a aplicação</td>
    </tr>
  </tbody>
</table>

<hr>

<h2 id="-regras-e-pontuação">🕹️ Regras e Pontuação</h2>

<table>
  <thead>
    <tr>
      <th align="left">Elemento</th>
      <th align="left">Pontuação</th>
      <th align="left">Efeito Especial</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Bumpers Centrais</strong></td>
      <td>100 × Multiplicador</td>
      <td>Impulso elástico radial +4.5</td>
    </tr>
    <tr>
      <td><strong>Kickers / Slingshots</strong></td>
      <td>50 × Multiplicador</td>
      <td>Repulsão angular rápida</td>
    </tr>
    <tr>
      <td><strong>Alvos Superiores (5x)</strong></td>
      <td>500 × Multiplicador</td>
      <td>Ilumina indicador neon</td>
    </tr>
    <tr>
      <td><strong>Combo Todos os 5 Alvos</strong></td>
      <td>+2.500 Pontos</td>
      <td>Aumenta Multiplicador e ativa MULTIBOLA</td>
    </tr>
    <tr>
      <td><strong>Bola Extra</strong></td>
      <td>Atingir 20.000 pts</td>
      <td>+1 Vida adicional</td>
    </tr>
  </tbody>
</table>

<blockquote>
  <p><strong>🔥 Multibola:</strong> Ao acender os 5 alvos de topo, o multiplicador de pontuação aumenta (até <strong>x5</strong>) e uma nova bola entra imediatamente em jogo pelo topo do ecrã!</p>
</blockquote>

<hr>

<h2 id="-como-executar">🚀 Como Executar</h2>

<h3>Pré-requisitos</h3>
<ul>
  <li>Python 3.10 ou superior instalado.</li>
</ul>

<h3>Passo a Passo</h3>
<pre><code># 1. Clonar o repositório
git clone https://github.com/Edinaldo-long/pinball.git
cd pinball

# 2. Instalar a dependência
pip install pygame

# 3. Executar a mesa
python pinball.py</code></pre>

<hr>

<h2>📁 Estrutura do Repositório</h2>

<pre><code>pinball/
│
├── pinball.py           # Código fonte completo do motor físico e renderização
├── requirements.txt     # Dependências mínimas (pygame)
├── .gitignore           # Exclusão de cache e recorde local
├── LICENSE              # Licença MIT
├── README.md            # Documentação técnica de apresentação
└── screenshots/
    └── gameplay.png     # Captura de ecrã da mesa em execução</code></pre>

<hr>

<h2>👤 Autor</h2>

<p>
  Desenvolvido por <strong>Edinaldo Santos de Almeida</strong><br>
  <a href="https://github.com/Edinaldo-long"><img src="https://img.shields.io/badge/GitHub-Edinaldo--long-181717?style=flat-square&logo=github" alt="GitHub"></a>
</p>

<hr>

<div align="center">
  <sub>Licenciado sob a Licença MIT. Desenvolvido para fins de estudo de engenharia de jogos, física computacional e computação gráfica 2D.</sub>
</div>
README_FINAL.html
A apresentar README_FINAL.html.
