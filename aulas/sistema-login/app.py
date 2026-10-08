from flask import Flask, request, render_template

"""
    A função render_template:

    1. procura o arquivo na pasta templates;
    2. processa o conteúdo com Jinja;
    3. produz o HTML final;
    4. permite que o Flask envie esse HTML ao navegador.

"""

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template(
        "index.html",
        nome="Bob"
    )

@app.route("/sobre")
def sobre():
    return render_template(
        "sobre.html",
        objetivo="Testando em outra rota"
    )

@app.route("/teste-metodo", methods=["GET", "POST"])
def teste_metodo():
    if request.method == "GET":
        return "RESPOSTA PARA GET"
    if request.method == "POST":
        return "RESPOSTA PARA POST"

@app.route("/exemplo-criado") # methods=["GET"] < - opcional, por padrão, se eu não escrever, será GET.
def exemplo_criado():
    return "CONTEÚDO", 201 # resposta apenas para fins didáticos, normalmente é utilizada para uma ação que realmente criou alguma coisa, normalmente por POST.

# 404 significa que a rota solicitada não foi encontrada. 405 significa que a rota foi encontrada, mas o método HTTP utilizado não é permitido nela.
