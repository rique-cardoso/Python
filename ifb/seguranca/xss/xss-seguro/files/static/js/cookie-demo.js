// ════════════════════════════════════════════════════════
// cookie-demo.js — Demonstrações de roubo de cookie via XSS
// INTENCIONALMENTE VULNERÁVEL — fins acadêmicos
// ════════════════════════════════════════════════════════

// ── Exibir cookies via JS ──────────────────────────────
function showCookies() {
  var output = document.getElementById('cookie-result');
  output.style.display = 'block';
  // ⚠️ document.cookie acessível porque flag HttpOnly está AUSENTE
  output.textContent = 'document.cookie = "' + document.cookie + '"';
}

// ── Simular exfiltração de cookie ─────────────────────
function simulateTheft() {
  // ⚠️ Simula o que um atacante faria com XSS armazenado
  // Em um cenário real, a URL apontaria para servidor do atacante
  var stolen = document.cookie;
  var img = new Image();
  img.src = '/cookie-demo?stolen=' + encodeURIComponent(stolen);
  // Também redireciona para mostrar visualmente
  window.location.href = '/cookie-demo?stolen=' + encodeURIComponent(stolen);
}

// ── Keylogger de demonstração ─────────────────────────
var keyloggerActive = false;
var keylogBuffer = '';

function startKeylogger() {
  var output = document.getElementById('keylog-output');

  if (keyloggerActive) {
    document.removeEventListener('keypress', keylogHandler);
    keyloggerActive = false;
    output.style.display = 'none';
    event.target.textContent = 'Ativar Keylogger Demo';
    event.target.style.borderColor = '';
    return;
  }

  keyloggerActive = true;
  output.style.display = 'block';
  output.innerHTML = '<em style="color:#5a6080">Keylogger ativo — comece a digitar...</em>';
  event.target.textContent = '⏹ Desativar Keylogger';
  event.target.style.borderColor = '#69ff47';

  document.addEventListener('keypress', keylogHandler);
}

function keylogHandler(e) {
  if (!keyloggerActive) return;
  var output = document.getElementById('keylog-output');
  keylogBuffer += e.key;
  output.innerHTML = '<span style="color:#69ff47">Capturado:</span> <span style="color:#ffd740">' +
    escapeHtmlSafe(keylogBuffer) + '</span>';
  output.scrollTop = output.scrollHeight;
}

// Função segura apenas para exibição interna
function escapeHtmlSafe(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}
