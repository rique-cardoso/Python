from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from werkzeug.security import generate_password_hash, check_password_hash

# Criar db
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

"""
    A função render_template:

    1. procura o arquivo na pasta templates;
    2. processa o conteúdo com Jinja;
    3. produz o HTML final;
    4. permite que o Flask envie esse HTML ao navegador.

"""
# Criar app
app = Flask(__name__)

# Configurar URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"

# Inicializar db com app
db.init_app(app)

# Definir modelos
""" class Teste(db.Model):
    __tablename__ = "testes"

    id: Mapped[int] = mapped_column(primary_key=True)
    texto: Mapped[str] = mapped_column(nullable=False) """

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(
        String(320),
        unique=True,
        nullable=False
    )

    senha_hash: Mapped[str] = mapped_column(
        String(512),
        nullable=False
    )

    def definir_senha(self, senha: str) -> None:
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha: str) -> bool:
        return check_password_hash(self.senha_hash, senha)

    def __repr__(self) -> str:
        return f"<Usuario id={self.id} email={self.email!r}>"
    
# Executar create_all()
with app.app_context():
    db.create_all()

# Declarar rotas
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

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        email = request.form.get("email").strip()
        senha = request.form.get("senha", "")
        # Duas formas para recuperar campos do formulário:
        # 1. email = request.form["email"] # se o campo não existir, gera KeyError
        # 2. email = request.form.get("email") # se o campo não existir, retorna None
        # Também podemos definir um valor-padrão:
        # 3. email = request.form.get("email", "valor-padrão")
        # print(request.form)
        if not email or not senha:
            return render_template(
                "login.html",
                mensagem="E-mail e senha são obrigatórios.",
                email=email
            ), 400
        return render_template(
            "login.html",
            mensagem="Dados recebidos com sucesso!"
        )