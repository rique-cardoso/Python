from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "<h1>Aplicação modificada</h1>"

@app.route("/sobre")
def sobre():
    return "<h1>Sobre: este é um projeto de estudo</h1>"

@app.route("/teste-metodo", methods=["GET", "POST"])
def teste_metodo():
    if request.method == "GET":
        return "RESPOSTA PARA GET"
    if request.method == "POST":
        return "RESPOSTA PARA POST"

@app.route("/exemplo-criado", methods=["GET"])
def exemplo_criado():
    return "CONTEÚDO", 201
