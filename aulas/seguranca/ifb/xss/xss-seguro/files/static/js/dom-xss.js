// ════════════════════════════════════════════════════════
// dom-xss.js — INTENCIONALMENTE VULNERÁVEL (fins acadêmicos)
// Demonstra sinks DOM vulneráveis a XSS
// ════════════════════════════════════════════════════════

// ── Sink 1: location.hash → innerHTML ──────────────────
// ⚠️ VULNERÁVEL: lê o hash da URL e insere via innerHTML sem sanitização
function processHash() {
  var hash = window.location.hash.slice(1); // remove o '#'
  if (hash) {
    var decoded = decodeURIComponent(hash);
    var output = document.getElementById('hash-output');
    if (output) {
      // ⚠️ innerHTML — sink vulnerável
      output.innerHTML = '<strong>Hash recebido:</strong> ' + decoded;
    }
  }
}

// ── Sink 2: location.search → innerHTML ────────────────
// ⚠️ VULNERÁVEL: lê parâmetro ?msg= e insere via innerHTML
function processSearch() {
  var params = new URLSearchParams(window.location.search);
  var msg = params.get('msg');
  if (msg) {
    var output = document.getElementById('search-output');
    if (output) {
      // ⚠️ innerHTML — sink vulnerável
      output.innerHTML = '<strong>Mensagem recebida:</strong> ' + msg;
    }
  }
}

// ── Sink 3: document.write ─────────────────────────────
// ⚠️ VULNERÁVEL: escreve input do usuário diretamente via document.write
function doDocWrite() {
  var input = document.getElementById('docwrite-input').value;
  var frame = document.getElementById('docwrite-frame');
  var doc = frame.contentDocument || frame.contentWindow.document;
  doc.open();
  // ⚠️ document.write — sink vulnerável
  doc.write('<style>body{background:#080810;color:#c8d0e8;font-family:monospace;padding:8px;font-size:13px}</style>' + input);
  doc.close();
}

// ── Sink 4: eval ───────────────────────────────────────
// ⚠️ EXTREMAMENTE VULNERÁVEL: executa input via eval()
function doEval() {
  var input = document.getElementById('eval-input').value;
  try {
    // ⚠️ eval() — sink altamente vulnerável
    eval(input);
  } catch(e) {
    alert('Erro no eval: ' + e.message);
  }
}

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

// ── Auto-processar ao carregar a página ────────────────
window.addEventListener('load', function() {
  processHash();
  processSearch();
});

// ⚠️ Também processa quando o hash muda (sem reload)
window.addEventListener('hashchange', function() {
  processHash();
});
