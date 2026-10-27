from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError

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
        if not self.senha_hash:
            return False
        
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

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "GET":
        return render_template("cadastro.html")

    email = request.form.get("email", "").strip().lower()
    senha = request.form.get("senha", "")
    confirmacao_senha = request.form.get("confirmacao_senha", "")

    # Validação dos campos obrigatórios
    if not email or not senha or not confirmacao_senha:
        return render_template(
            "cadastro.html",
            mensagem="Preencha todos os campos.",
            email=email
        ), 400
    # Validação do tamnho do e-mail
    """Como o modelo usa String(320) é necessário validar o tamanho do e-mail antes de tentar salvar no banco, caso contrário, o SQLAlchemy vai gerar um erro de violação de restrição de tamanho."""
    if len(email) > 320:
        return render_template(
            "cadastro.html",
            mensagem="O e-mail informado é muito longo.",
            email=email
        ), 400
    # Validação de senha
    if len(senha) < 8:
        return render_template(
            "cadastro.html",
            mensagem="A senha deve ter pelo menos 8 caracteres.",
            email=email
        ), 400
    if len(senha) > 128:
        return render_template(
            "cadastro.html",
            mensagem="A senha ultrapassa o tamanho permitido.",
            email=email
        ), 400
    if senha != confirmacao_senha:
        return render_template(
            "cadastro.html",
            mensagem="As senhas não conferem.",
            email=email
        ), 400
    # Consulta usuario existente
    usuario_existente = db.session.execute(
        db.select(Usuario).where(Usuario.email == email)
    ).scalar_one_or_none()
    if usuario_existente is not None:
        return render_template(
            "cadastro.html",
            mensagem="Já existe um usuário cadastrado com esse e-mail.",
            email=email
        ), 409
    # Novo usuario
    novo_usuario = Usuario(email=email)
    novo_usuario.definir_senha(senha)
    db.session.add(novo_usuario)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return render_template(
            "cadastro.html",
            mensagem="Não foi possível criar a conta com os dados informados.",
            email=email
        ), 409

    return redirect(url_for("login"))
    