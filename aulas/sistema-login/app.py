from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "<h1>Aplicação modificada</h1>"

@app.route("/sobre")
def sobre():
    return "<h1>Sobre: este é um projeto de estudo</h1>"