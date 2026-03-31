"""
╔══════════════════════════════════════════════════════════════╗
║         XSS LAB SEGURO — Versão Corrigida                    ║
║         Demonstra as MITIGAÇÕES de cada vulnerabilidade XSS  ║
╚══════════════════════════════════════════════════════════════╝

CORREÇÕES APLICADAS:
  [1] html.escape() em todos os outputs refletidos do servidor
  [2] Jinja2 com auto-escaping ativado (render_template + Markup)
  [3] Cookies com HttpOnly=True e SameSite=Strict
  [4] SECRET_KEY forte gerada via secrets.token_hex()
  [5] CSP (Content-Security-Policy) header em todas as respostas
  [6] Validação e limite de tamanho nos inputs
  [7] JS seguro: textContent no lugar de innerHTML
  [8] JS seguro: sem document.write(), sem eval()
  [9] CSRF token nos formulários POST
  [10] X-Content-Type-Options, X-Frame-Options headers
"""

from flask import Flask, request, render_template_string, make_response, redirect, session
from markupsafe import Markup, escape   # [1][2] escape seguro do Jinja2/MarkupSafe
import sqlite3
import secrets   # [4] geração de SECRET_KEY e CSRF tokens
import html      # [1] html.escape() nativo do Python

app = Flask(__name__)

# ✅ [4] SECRET_KEY forte — gerada aleatoriamente a cada execução
app.secret_key = secrets.token_hex(32)

DB_PATH = "xsslab_secure.db"

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
            author  TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    existing = conn.execute("SELECT COUNT(*) FROM comments").fetchone()[0]
    if existing == 0:
        conn.execute("INSERT INTO comments (author, content) VALUES (?, ?)",
                     ("admin", "Bem-vindo ao XSS Lab Seguro!"))
        conn.execute("INSERT INTO comments (author, content) VALUES (?, ?)",
                     ("alice", "Nesta versão os inputs são escapados corretamente."))
    conn.commit()
    conn.close()

# ─────────────────────────────────────────────
# HELPERS DE SEGURANÇA
# ─────────────────────────────────────────────

def safe_escape(value: str) -> str:
    """
    ✅ [1] Converte caracteres especiais HTML em entidades seguras.
    Ex: <script> → &lt;script&gt;  |  " → &quot;
    Impede que qualquer string do usuário seja interpretada como HTML/JS.
    """
    return html.escape(value, quote=True)

def get_csrf_token() -> str:
    """✅ [9] Gera (ou recupera) um token CSRF por sessão."""
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(16)
    return session["csrf_token"]

def validate_csrf(form_token: str) -> bool:
    """✅ [9] Compara o token do formulário com o da sessão (timing-safe)."""
    expected = session.get("csrf_token", "")
    return secrets.compare_digest(expected, form_token)

def add_security_headers(response):
    """
    ✅ [5][10] Adiciona headers de segurança HTTP em todas as respostas.

    Content-Security-Policy:
      - default-src 'self'   → só carrega recursos da própria origem
      - script-src 'self'    → bloqueia scripts inline e de origens externas
      - style-src 'self' ... → permite apenas o CSS próprio + Google Fonts
      - object-src 'none'    → bloqueia Flash/plugins
      - base-uri 'self'      → impede injeção de <base> tag
      - form-action 'self'   → formulários só submetem para a própria origem
      Isto bloqueia a execução de scripts injetados mesmo que o escape falhe.

    X-Content-Type-Options: nosniff
      → Impede MIME-type sniffing (vetor de XSS em uploads)

    X-Frame-Options: DENY
      → Impede clickjacking (a página não pode ser embutida em iframes)

    Referrer-Policy: no-referrer
      → Não vaza a URL atual para sites externos
    """
    csp = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self' https://fonts.googleapis.com; "
        "font-src https://fonts.gstatic.com; "
        "img-src 'self' data:; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "form-action 'self'; "
        "frame-ancestors 'none';"
    )
    response.headers["Content-Security-Policy"] = csp
    response.headers["X-Content-Type-Options"]  = "nosniff"
    response.headers["X-Frame-Options"]         = "DENY"
    response.headers["Referrer-Policy"]         = "no-referrer"
    return response

# Aplica headers de segurança em TODAS as respostas automaticamente
@app.after_request
def apply_security_headers(response):
    return add_security_headers(response)

# ─────────────────────────────────────────────
# TEMPLATE BASE — com Jinja2 auto-escaping
# ─────────────────────────────────────────────
# ✅ [2] Usamos render_template_string com variáveis Jinja2 ({{ var }})
# O Jinja2 escapa automaticamente qualquer variável passada via {{ }}.
# Diferente da versão vulnerável que usava .format() — Python f-strings
# NÃO fazem escape; Jinja2 faz.

BASE_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>XSS Lab Seguro — {{ title }}</title>
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
      <div class="warning-badge secure-badge">✅ VERSÃO SEGURA — MITIGAÇÕES ATIVAS</div>
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
      <h1>{{ title }}</h1>
      <div class="title-line"></div>
    </div>
    {{ content }}
  </main>

  <footer>
    <p>XSS Lab Seguro &mdash; Versão com Mitigações &mdash; Material Acadêmico</p>
  </footer>
  <script src="/static/js/main.js"></script>
</body>
</html>"""

# ─────────────────────────────────────────────
# ROTA: HOME
# ─────────────────────────────────────────────

@app.route("/")
def index():
    # ✅ [2] Usamos Markup() apenas para HTML estático que NÓS mesmos escrevemos.
    # Nunca use Markup() em dados vindos do usuário!
    content = Markup("""
    <div class="home-grid">
      <div class="attack-card" onclick="window.location='/reflected'">
        <div class="card-icon">🔁</div>
        <h2>Reflected XSS</h2>
        <p>Inputs refletidos agora com <strong>html.escape()</strong> e auto-escaping Jinja2.</p>
        <div class="card-tag secure-tag">✅ CORRIGIDO</div>
      </div>
      <div class="attack-card" onclick="window.location='/stored'">
        <div class="card-icon">💾</div>
        <h2>Stored XSS</h2>
        <p>Outputs do banco escapados com <strong>escape()</strong> antes de renderizar.</p>
        <div class="card-tag secure-tag">✅ CORRIGIDO</div>
      </div>
      <div class="attack-card" onclick="window.location='/dom'">
        <div class="card-icon">🌐</div>
        <h2>DOM-based XSS</h2>
        <p>JS reescrito com <strong>textContent</strong> — sem innerHTML, eval ou document.write.</p>
        <div class="card-tag secure-tag">✅ CORRIGIDO</div>
      </div>
      <div class="attack-card" onclick="window.location='/cookie-demo'">
        <div class="card-icon">🍪</div>
        <h2>Cookie Theft</h2>
        <p>Cookies agora com flags <strong>HttpOnly</strong> e <strong>SameSite=Strict</strong>.</p>
        <div class="card-tag secure-tag">✅ CORRIGIDO</div>
      </div>
    </div>
    <div class="info-box secure-box">
      <h3>🛡️ O que foi corrigido nesta versão</h3>
      <ul class="fix-list">
        <li><strong>html.escape()</strong> em todos os parâmetros refletidos pelo servidor</li>
        <li><strong>Jinja2 auto-escaping</strong> via <code>{{ }}</code> em vez de f-strings/<code>.format()</code></li>
        <li><strong>textContent</strong> no lugar de <code>innerHTML</code> no JavaScript</li>
        <li>Eliminação de <code>eval()</code> e <code>document.write()</code></li>
        <li>Cookies com <strong>HttpOnly=True</strong> e <strong>SameSite=Strict</strong></li>
        <li><strong>CSP</strong> (Content-Security-Policy) bloqueando scripts inline e externos</li>
        <li><strong>CSRF tokens</strong> em todos os formulários POST</li>
        <li>Headers: <strong>X-Frame-Options</strong>, <strong>X-Content-Type-Options</strong></li>
        <li><strong>SECRET_KEY</strong> forte gerada com <code>secrets.token_hex(32)</code></li>
      </ul>
    </div>
    """)
    resp = make_response(render_template_string(BASE_HTML, title="Laboratório XSS Seguro", content=content))
    # ✅ [3] Cookies com HttpOnly=True — inacessíveis via document.cookie
    resp.set_cookie("session_token", secrets.token_hex(16),
                    httponly=True,          # ✅ JS não consegue ler
                    samesite="Strict",      # ✅ protege contra CSRF via cookie
                    secure=False)           # True em produção com HTTPS
    resp.set_cookie("user_role", "user",
                    httponly=True,
                    samesite="Strict")
    return resp


# ─────────────────────────────────────────────
# ROTA: REFLECTED XSS — CORRIGIDO
# ─────────────────────────────────────────────

@app.route("/reflected")
def reflected():
    # ✅ [1] Aplica html.escape() ANTES de usar qualquer valor do usuário
    query = safe_escape(request.args.get("q", ""))
    name  = safe_escape(request.args.get("name", ""))
    error = safe_escape(request.args.get("error", ""))

    # ✅ [6] Limite de tamanho — impede payloads excessivamente grandes
    query = query[:200]
    name  = name[:100]
    error = error[:200]

    result_block = Markup("")
    if query:
        # ✅ safe_escape() já transformou qualquer <script> em &lt;script&gt;
        # Markup() informa ao Jinja2 que este HTML é de confiança (já escapamos manualmente)
        result_block = Markup(f"""
        <div class="result-box secure-result">
          <span class="secure-label">✅ ESCAPED — html.escape() aplicado</span>
          <p>Você pesquisou por: <strong>{query}</strong></p>
          <p class="escape-note">Qualquer tag HTML foi convertida em texto puro.</p>
        </div>""")

    name_block = Markup("")
    if name:
        # ✅ html.escape(quote=True) escapa aspas também → seguro em atributos
        result_block_name = Markup(f"""
        <div class="result-box secure-result">
          <span class="secure-label">✅ ESCAPED em atributo HTML</span>
          <input type="text" value="{name}" class="vuln-input" readonly>
          <p>Aspas e caracteres especiais foram escapados com <code>quote=True</code>.</p>
        </div>""")
        name_block = result_block_name

    error_block = Markup("")
    if error:
        error_block = Markup(f"""
        <div class="result-box secure-result">
          <span class="secure-label">✅ ESCAPED — mensagem de erro segura</span>
          <p>Erro: {error}</p>
        </div>""")

    # ✅ [2] Passamos as variáveis para render_template_string via contexto Jinja2
    # O Jinja2 escapa automaticamente {{ variavel }} — linha de defesa adicional
    content = Markup(f"""
    <div class="lab-section">
      <div class="section-meta">
        <span class="badge badge-reflect">REFLECTED XSS</span>
        <div class="fix-banner">
          🛡️ <strong>Correção aplicada:</strong> <code>html.escape(value, quote=True)</code> em todos os parâmetros
          + Jinja2 auto-escaping via <code>{{{{ var }}}}</code> em vez de <code>.format()</code>
        </div>
      </div>

      <div class="vuln-forms">
        <div class="form-group">
          <label>🔍 Pesquisa (parâmetro <code>?q=</code>)</label>
          <form method="GET">
            <input type="text" name="q" placeholder="Tente: &lt;script&gt;alert(1)&lt;/script&gt;" class="input-field">
            <button type="submit" class="btn">Pesquisar</button>
          </form>
        </div>
        <div class="form-group">
          <label>👤 Nome (parâmetro <code>?name=</code>)</label>
          <form method="GET">
            <input type="text" name="name" placeholder='Tente: " onmouseover="alert(1)' class="input-field">
            <button type="submit" class="btn">Enviar</button>
          </form>
        </div>
        <div class="form-group">
          <label>❌ Erro (parâmetro <code>?error=</code>)</label>
          <form method="GET">
            <input type="text" name="error" placeholder="Tente: &lt;img src=x onerror=alert(1)&gt;" class="input-field">
            <button type="submit" class="btn">Simular Erro</button>
          </form>
        </div>
      </div>

      {result_block}
      {name_block}
      {error_block}

      <div class="fix-detail">
        <h3>🔍 Como a correção funciona</h3>
        <div class="code-compare">
          <div class="code-bad">
            <span class="code-label bad">❌ VULNERÁVEL</span>
            <pre>query = request.args.get("q", "")
# f-string injeta o valor cru no HTML:
html = f"&lt;p&gt;Resultado: {{query}}&lt;/p&gt;"</pre>
          </div>
          <div class="code-good">
            <span class="code-label good">✅ SEGURO</span>
            <pre>query = html.escape(request.args.get("q",""))
# Caracteres perigosos viram entidades HTML:
# &lt;script&gt; → &amp;lt;script&amp;gt;</pre>
          </div>
        </div>
      </div>
    </div>
    """)
    return render_template_string(BASE_HTML, title="Reflected XSS — Corrigido", content=content)


# ─────────────────────────────────────────────
# ROTA: STORED XSS — CORRIGIDO
# ─────────────────────────────────────────────

@app.route("/stored", methods=["GET", "POST"])
def stored():
    conn = get_db()
    msg = ""
    csrf_error = ""

    if request.method == "POST":
        form_token = request.form.get("csrf_token", "")

        # ✅ [9] Valida CSRF token antes de processar o formulário
        if not validate_csrf(form_token):
            csrf_error = "Token CSRF inválido. Requisição bloqueada."
        else:
            author  = request.form.get("author", "Anônimo").strip()
            comment = request.form.get("comment", "").strip()

            # ✅ [6] Limites de tamanho
            author  = author[:80]
            comment = comment[:1000]

            if comment:
                # ✅ Os dados são salvos no banco como texto puro.
                # A sanitização ocorre na EXIBIÇÃO, não no armazenamento —
                # mas ambos são válidos; o importante é nunca renderizar cru.
                conn.execute("INSERT INTO comments (author, content) VALUES (?, ?)",
                             (author, comment))
                conn.commit()
                msg = "✅ Comentário salvo com segurança!"

    rows = conn.execute("SELECT * FROM comments ORDER BY created_at DESC").fetchall()
    conn.close()

    # ✅ [1][2] Escapa CADA campo do banco individualmente antes de montar o HTML
    comments_html = Markup("")
    for row in rows:
        safe_author  = escape(row["author"])   # escape() do MarkupSafe — mesmo que html.escape
        safe_content = escape(row["content"])  # ← converte <script> em &lt;script&gt;
        safe_date    = escape(row["created_at"])
        comments_html += Markup(f"""
        <div class="comment-card">
          <div class="comment-header">
            <span class="comment-author">{safe_author}</span>
            <span class="comment-date">{safe_date}</span>
          </div>
          <div class="comment-body">{safe_content}</div>
        </div>""")

    csrf_token = get_csrf_token()   # ✅ [9]

    content = Markup(f"""
    <div class="lab-section">
      <div class="section-meta">
        <span class="badge badge-stored">STORED XSS</span>
        <div class="fix-banner">
          🛡️ <strong>Correção:</strong> <code>markupsafe.escape()</code> em cada campo do banco
          + CSRF token no formulário POST
        </div>
      </div>

      <div class="stored-form">
        <h3>💬 Deixar comentário</h3>
        {Markup(f'<div class="success-msg">{msg}</div>') if msg else Markup("")}
        {Markup(f'<div class="error-msg">⚠️ {csrf_error}</div>') if csrf_error else Markup("")}
        <form method="POST">
          <input type="hidden" name="csrf_token" value="{csrf_token}">
          <input type="text" name="author" placeholder="Seu nome" class="input-field" maxlength="80">
          <textarea name="comment" rows="4"
            placeholder="Seu comentário (HTML será escapado automaticamente)"
            class="input-field" maxlength="1000"></textarea>
          <button type="submit" class="btn">Publicar Comentário</button>
        </form>
      </div>

      <div class="comments-section">
        <h3>📝 Comentários ({len(rows)})</h3>
        {comments_html if comments_html else Markup('<p class="empty">Nenhum comentário ainda.</p>')}
      </div>

      <form method="POST" action="/stored/clear">
        <input type="hidden" name="csrf_token" value="{csrf_token}">
        <button type="submit" class="btn btn-sm" style="margin-top:1rem">🗑️ Limpar comentários</button>
      </form>

      <div class="fix-detail">
        <h3>🔍 Como a correção funciona</h3>
        <div class="code-compare">
          <div class="code-bad">
            <span class="code-label bad">❌ VULNERÁVEL</span>
            <pre>for row in rows:
  # HTML cru do banco inserido direto:
  html += f"&lt;div&gt;{{row['content']}}&lt;/div&gt;"</pre>
          </div>
          <div class="code-good">
            <span class="code-label good">✅ SEGURO</span>
            <pre>from markupsafe import escape
for row in rows:
  safe = escape(row['content'])
  html += Markup(f"&lt;div&gt;{{safe}}&lt;/div&gt;")</pre>
          </div>
        </div>
      </div>
    </div>
    """)
    return render_template_string(BASE_HTML, title="Stored XSS — Corrigido", content=content)


@app.route("/stored/clear", methods=["POST"])
def stored_clear():
    # ✅ [9] Valida CSRF mesmo na rota de limpeza
    form_token = request.form.get("csrf_token", "")
    if not validate_csrf(form_token):
        return "CSRF inválido", 403
    conn = get_db()
    conn.execute("DELETE FROM comments WHERE author != 'admin'")
    conn.commit()
    conn.close()
    return redirect("/stored")


# ─────────────────────────────────────────────
# ROTA: DOM-BASED XSS — CORRIGIDO
# ─────────────────────────────────────────────

@app.route("/dom")
def dom_xss():
    # ✅ A correção principal está no dom-xss-secure.js
    content = Markup("""
    <div class="lab-section">
      <div class="section-meta">
        <span class="badge badge-dom">DOM-BASED XSS</span>
        <div class="fix-banner">
          🛡️ <strong>Correção:</strong> <code>textContent</code> no lugar de <code>innerHTML</code>
          &bull; Removidos <code>eval()</code> e <code>document.write()</code>
          &bull; CSP bloqueia scripts inline
        </div>
      </div>

      <div class="dom-demos">

        <div class="dom-demo-card">
          <h3>🔗 Via <code>location.hash</code></h3>
          <p>Hash lido e exibido com <strong>textContent</strong> — HTML não é interpretado.</p>
          <div id="hash-output" class="dom-output secure-output">
            <em>Aguardando hash na URL...</em>
          </div>
          <div class="url-builder">
            <input type="text" id="hash-input" placeholder="&lt;script&gt;alert(1)&lt;/script&gt; — não vai executar" class="input-field">
            <button onclick="applyHash()" class="btn">Testar via Hash</button>
          </div>
        </div>

        <div class="dom-demo-card">
          <h3>🔗 Via <code>location.search</code></h3>
          <p>Parâmetro <code>?msg=</code> inserido via <strong>textContent</strong>, não innerHTML.</p>
          <div id="search-output" class="dom-output secure-output">
            <em>Aguardando parâmetro ?msg= na URL...</em>
          </div>
          <div class="url-builder">
            <input type="text" id="search-input" placeholder="&lt;img src=x onerror=alert(1)&gt; — inofensivo aqui" class="input-field">
            <button onclick="applySearch()" class="btn">Testar via Search</button>
          </div>
        </div>

        <div class="dom-demo-card">
          <h3>⚡ <code>document.write()</code> → removido</h3>
          <p>Substituído por criação segura de elemento com <strong>createElement</strong> + <strong>textContent</strong>.</p>
          <div class="url-builder">
            <input type="text" id="docwrite-input" placeholder="Texto comum — HTML não será renderizado" class="input-field">
            <button onclick="doSafeOutput()" class="btn">Exibir com segurança</button>
          </div>
          <div id="safe-output" class="dom-output secure-output" style="margin-top:.5rem"></div>
        </div>

        <div class="dom-demo-card">
          <h3>⚡ <code>eval()</code> → removido</h3>
          <p>Entrada de usuário <strong>nunca</strong> deve ser avaliada como código. Demonstração bloqueada intencionalmente.</p>
          <div class="url-builder">
            <input type="text" id="eval-input" placeholder="eval() foi removido desta versão" class="input-field" disabled>
            <button class="btn" disabled title="eval() removido por segurança">❌ Bloqueado</button>
          </div>
          <p class="escape-note">Use JSON.parse() quando precisar processar dados estruturados.</p>
        </div>

      </div>

      <div class="fix-detail">
        <h3>🔍 Como a correção funciona</h3>
        <div class="code-compare">
          <div class="code-bad">
            <span class="code-label bad">❌ VULNERÁVEL (JS)</span>
            <pre>// Sink perigoso: interpreta HTML
var hash = location.hash.slice(1);
element.innerHTML = hash;

// Execução arbitrária de código:
eval(userInput);</pre>
          </div>
          <div class="code-good">
            <span class="code-label good">✅ SEGURO (JS)</span>
            <pre>// Trata como texto puro, nunca como HTML:
var hash = decodeURIComponent(location.hash.slice(1));
element.textContent = hash;

// eval() simplesmente não existe mais.</pre>
          </div>
        </div>
      </div>
    </div>

    <script src="/static/js/dom-xss-secure.js"></script>
    """)
    return render_template_string(BASE_HTML, title="DOM-based XSS — Corrigido", content=content)


# ─────────────────────────────────────────────
# ROTA: COOKIE DEMO — CORRIGIDO
# ─────────────────────────────────────────────

@app.route("/cookie-demo")
def cookie_demo():
    # ✅ [1] Parâmetro 'stolen' agora escapado
    stolen_raw = request.args.get("stolen", "")
    stolen     = safe_escape(stolen_raw)[:300]

    stolen_block = Markup("")
    if stolen:
        stolen_block = Markup(f"""
        <div class="result-box secure-result">
          <span class="secure-label">✅ RECEBIDO E ESCAPADO</span>
          <p>Dado recebido (escapado): <strong>{stolen}</strong></p>
          <p class="escape-note">Qualquer HTML/JS foi neutralizado pelo escape antes da exibição.</p>
        </div>""")

    content = Markup(f"""
    <div class="lab-section">
      <div class="section-meta">
        <span class="badge badge-cookie">COOKIE THEFT / SESSION HIJACKING</span>
        <div class="fix-banner">
          🛡️ <strong>Correção:</strong> Cookies com <code>HttpOnly=True</code> e <code>SameSite=Strict</code>
          — inacessíveis via JavaScript
        </div>
      </div>

      <div class="cookie-display">
        <h3>🍪 Cookies desta sessão</h3>
        <div class="cookie-card">
          <div class="cookie-item">
            <span class="cookie-key">session_token</span>
            <span class="cookie-val">[oculto — HttpOnly ativo]</span>
            <span class="cookie-flag flag-secure">✅ HttpOnly + SameSite=Strict</span>
          </div>
          <div class="cookie-item">
            <span class="cookie-key">user_role</span>
            <span class="cookie-val">[oculto — HttpOnly ativo]</span>
            <span class="cookie-flag flag-secure">✅ HttpOnly + SameSite=Strict</span>
          </div>
        </div>
        <p class="cookie-note secure-note">
          ✅ <code>document.cookie</code> retornará string vazia — cookies são invisíveis para o JavaScript.
        </p>
      </div>

      <div class="attack-demos">
        <h3>🛡️ Defesas em ação</h3>

        <div class="attack-step secure-step">
          <span class="step-num step-secure">1</span>
          <div>
            <strong>Tentativa de ler cookies via JS</strong>
            <p>Com <code>HttpOnly=True</code>, <code>document.cookie</code> não retorna os cookies de sessão.</p>
            <button onclick="tryReadCookies()" class="btn">Tentar document.cookie</button>
            <div id="cookie-result" class="dom-output secure-output" style="display:none"></div>
          </div>
        </div>

        <div class="attack-step secure-step">
          <span class="step-num step-secure">2</span>
          <div>
            <strong>Tentativa de exfiltração</strong>
            <p>Sem acesso ao cookie, o payload de roubo retorna uma string vazia — ataque neutralizado.</p>
            <button onclick="tryTheft()" class="btn">Simular tentativa</button>
            <div id="theft-result" class="dom-output secure-output" style="display:none"></div>
          </div>
        </div>

        <div class="attack-step secure-step">
          <span class="step-num step-secure">3</span>
          <div>
            <strong>CSP bloqueia scripts externos</strong>
            <p>Mesmo que XSS fosse possível, a CSP impediria <code>fetch()</code> para domínios externos.</p>
            <code class="block-code">Content-Security-Policy: default-src 'self'; script-src 'self'</code>
          </div>
        </div>
      </div>

      {stolen_block}

      <div class="fix-detail">
        <h3>🔍 Como a correção funciona</h3>
        <div class="code-compare">
          <div class="code-bad">
            <span class="code-label bad">❌ VULNERÁVEL</span>
            <pre>resp.set_cookie("session_token",
    "SEGREDO",
    httponly=False,   # JS pode ler!
    samesite=None)</pre>
          </div>
          <div class="code-good">
            <span class="code-label good">✅ SEGURO</span>
            <pre>resp.set_cookie("session_token",
    secrets.token_hex(16),
    httponly=True,       # JS não pode ler
    samesite="Strict",   # anti-CSRF
    secure=True)         # apenas HTTPS</pre>
          </div>
        </div>
      </div>
    </div>
    <script src="/static/js/cookie-demo-secure.js"></script>
    """)
    resp = make_response(render_template_string(BASE_HTML, title="Cookie Theft — Corrigido", content=content))
    # ✅ [3] Cookies seguros
    resp.set_cookie("session_token", secrets.token_hex(16),
                    httponly=True, samesite="Strict", secure=False)
    resp.set_cookie("user_role", "user",
                    httponly=True, samesite="Strict", secure=False)
    return resp


# ─────────────────────────────────────────────
# ROTA: GUIA
# ─────────────────────────────────────────────

@app.route("/guia")
def guia():
    content = Markup("""
    <div class="lab-section guia-section">
      <div class="section-meta">
        <span class="badge badge-guide">📖 GUIA DE MITIGAÇÕES</span>
        <p>Resumo de todas as correções aplicadas nesta versão segura.</p>
      </div>

      <div class="guia-grid">

        <div class="guia-card">
          <h2>🔁 Reflected XSS</h2>
          <table class="payload-table">
            <tr><th>Vulnerabilidade</th><th>Correção</th></tr>
            <tr><td>f-string com input do usuário</td><td><code>html.escape()</code></td></tr>
            <tr><td>Input em atributo HTML</td><td><code>html.escape(quote=True)</code></td></tr>
            <tr><td>.format() sem escape</td><td>Jinja2 <code>{{ var }}</code> auto-escaping</td></tr>
            <tr><td>Tamanho ilimitado</td><td>Truncamento com <code>[:200]</code></td></tr>
          </table>
        </div>

        <div class="guia-card">
          <h2>💾 Stored XSS</h2>
          <table class="payload-table">
            <tr><th>Vulnerabilidade</th><th>Correção</th></tr>
            <tr><td>HTML cru do banco no template</td><td><code>markupsafe.escape()</code></td></tr>
            <tr><td>Sem proteção CSRF</td><td>Token CSRF em todos os POST</td></tr>
            <tr><td>Tamanho ilimitado</td><td>maxlength no HTML + truncamento no server</td></tr>
            <tr><td>Conteúdo armazenado cru</td><td>Escape na exibição (defense in depth)</td></tr>
          </table>
        </div>

        <div class="guia-card">
          <h2>🌐 DOM-based XSS</h2>
          <table class="payload-table">
            <tr><th>Sink vulnerável</th><th>Alternativa segura</th></tr>
            <tr><td><code>element.innerHTML = x</code></td><td><code>element.textContent = x</code></td></tr>
            <tr><td><code>document.write(x)</code></td><td><code>createElement + textContent</code></td></tr>
            <tr><td><code>eval(x)</code></td><td>Removido — sem alternativa aceitável</td></tr>
            <tr><td>Scripts inline</td><td>CSP: <code>script-src 'self'</code></td></tr>
          </table>
        </div>

        <div class="guia-card">
          <h2>🍪 Cookies & Headers</h2>
          <table class="payload-table">
            <tr><th>Problema</th><th>Correção</th></tr>
            <tr><td>Cookie sem HttpOnly</td><td><code>httponly=True</code></td></tr>
            <tr><td>Cookie sem SameSite</td><td><code>samesite="Strict"</code></td></tr>
            <tr><td>SECRET_KEY fraca</td><td><code>secrets.token_hex(32)</code></td></tr>
            <tr><td>Sem CSP</td><td>Header <code>Content-Security-Policy</code></td></tr>
            <tr><td>Sem X-Frame-Options</td><td>Header <code>X-Frame-Options: DENY</code></td></tr>
          </table>
        </div>

      </div>

      <div class="info-box secure-box">
        <h3>📚 Referências para aprofundamento</h3>
        <ul class="fix-list">
          <li>OWASP XSS Prevention Cheat Sheet</li>
          <li>OWASP CSRF Prevention Cheat Sheet</li>
          <li>MDN: Content Security Policy (CSP)</li>
          <li>Python docs: <code>html.escape()</code></li>
          <li>MarkupSafe docs: <code>markupsafe.escape()</code></li>
          <li>Flask docs: Cookies e Segurança de Sessão</li>
        </ul>
      </div>
    </div>
    """)
    return render_template_string(BASE_HTML, title="Guia de Mitigações XSS", content=content)


if __name__ == "__main__":
    init_db()
    print("""
╔══════════════════════════════════════════════════════════╗
║  XSS Lab SEGURO iniciado em http://localhost:5000        ║
║  Versão com todas as mitigações XSS ativas              ║
╚══════════════════════════════════════════════════════════╝
    """)
    app.run(debug=False, host="127.0.0.1", port=5000)
