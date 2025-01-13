from flask import Flask # importação da biblioteca flask
# antes da importação é necessário instalar utilizando o comando no terminal: pip install flask
app = Flask(__name__)

from views import *

# executando o código apenas quando eu estiver executando o arquivo diretamente
if __name__ == '__main__':
    app.run()