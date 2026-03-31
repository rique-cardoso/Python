// ════════════════════════════════════════════════════════
// cookie-demo-secure.js — VERSÃO SEGURA
// Demonstra que os ataques de roubo de cookie são neutralizados
// ════════════════════════════════════════════════════════

// ✅ Tentativa de ler cookies — retorna vazio por causa do HttpOnly
function tryReadCookies() {
  var output = document.getElementById('cookie-result');
  output.style.display = 'block';

  var cookies = document.cookie;

  if (cookies === '') {
    // ✅ HttpOnly funcionando: document.cookie não retorna nada
    output.textContent = 'document.cookie = "" (vazio) — HttpOnly bloqueou o acesso!';
    output.style.color = '#69ff47';
  } else {
    // Cookies não sensíveis ainda podem aparecer (ex: preferências sem HttpOnly)
    output.textContent = 'document.cookie = "' + cookies + '"';
    output.style.color = '#ffd740';
  }
}

// ✅ Tentativa de exfiltração — demonstra que é ineficaz
function tryTheft() {
  var output = document.getElementById('theft-result');
  output.style.display = 'block';

  // Sem HttpOnly, este seria o payload do atacante.
  // Com HttpOnly, document.cookie retorna string vazia.
  var stolenData = document.cookie;

  if (stolenData === '') {
    output.textContent =
      'Tentativa de roubo: document.cookie = "" — ' +
      'Nada para roubar! HttpOnly protegeu os cookies de sessão.';
    output.style.color = '#69ff47';
  } else {
    // Apenas cookies sem HttpOnly (não sensíveis)
    output.textContent =
      'Apenas cookies não-sensíveis visíveis: "' + stolenData + '"';
    output.style.color = '#ffd740';
  }
}
