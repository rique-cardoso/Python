// ════════════════════════════════════════════════════════
// dom-xss-secure.js — VERSÃO SEGURA
// Demonstra as correções para cada sink vulnerável
// ════════════════════════════════════════════════════════

// ✅ Sink 1 CORRIGIDO: location.hash → textContent (não innerHTML)
function processHash() {
  var hash = window.location.hash.slice(1);
  if (hash) {
    var decoded = decodeURIComponent(hash);
    var output = document.getElementById('hash-output');
    if (output) {
      // ✅ textContent trata o valor como texto puro.
      // Qualquer HTML/JS é exibido literalmente, nunca executado.
      output.textContent = 'Hash recebido: ' + decoded;
    }
  }
}

// ✅ Sink 2 CORRIGIDO: location.search → textContent (não innerHTML)
function processSearch() {
  var params = new URLSearchParams(window.location.search);
  var msg = params.get('msg');
  if (msg) {
    var output = document.getElementById('search-output');
    if (output) {
      // ✅ textContent — seguro contra qualquer payload HTML/JS
      output.textContent = 'Mensagem recebida: ' + msg;
    }
  }
}

// ✅ Sink 3 CORRIGIDO: createElement + textContent (sem document.write)
function doSafeOutput() {
  var input = document.getElementById('docwrite-input').value;
  var container = document.getElementById('safe-output');
  container.innerHTML = ''; // limpa
  var p = document.createElement('p');
  // ✅ textContent atribui texto puro — HTML é literalmente exibido como string
  p.textContent = input;
  p.style.color = '#c8d0e8';
  container.appendChild(p);
}

// ✅ Sink 4 CORRIGIDO: eval() foi completamente removido.
// Não há substituto seguro para eval() com input de usuário.
// Se precisar processar dados estruturados, use JSON.parse()
// com dados validados de uma fonte confiável.

// ── Botão: aplicar hash ────────────────────────────────
function applyHash() {
  var val = document.getElementById('hash-input').value;
  window.location.hash = encodeURIComponent(val);
  processHash();
}

// ── Botão: aplicar search ──────────────────────────────
function applySearch() {
  var val = document.getElementById('search-input').value;
  var url = window.location.pathname + '?msg=' + encodeURIComponent(val);
  window.history.pushState({}, '', url);
  processSearch();
}

// ── Auto-processar ao carregar ─────────────────────────
window.addEventListener('load', function () {
  processHash();
  processSearch();
});

window.addEventListener('hashchange', function () {
  processHash();
});
