import sqlite3
arquivo_db = 'bylearn.db'
def iniciar_conexao():
    conexao = None
    try:
        conexao = sqlite3.connect(arquivo_db)
    except sqlite3.Error as e:
        print('Ops... Deu um erro iniciando a conexão: ', e)
    return conexao
def fechar_conexao(conexao):
    if conexao:
        conexao.close()
def criar_tabela(conexao, sql_criar_tabela):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql_criar_tabela)
    except sqlite3.Error as e:
        print('Ops... Deu um erro criando a tabela: ', e)
def inserir_aluno(conexao, sql_inserir_aluno):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql_inserir_aluno)
        conexao.commit()
    except sqlite3.Error as e:
        print('Ops... Deu um erro inserindo dados: ', e)
def buscar_alunos(conexao, sql_buscar_alunos):
    alunos = None
    try:
        cursor = conexao.cursor()
        cursor.execute(sql_buscar_alunos)
        alunos = cursor.fetchall()
    except sqlite3.Error as e:
        print('Ops... Deu um erro exibindo dados: ', e)
    finally:
        return alunos
# Iniciando conexão
conexao = iniciar_conexao()
# Criando a tabela
sql_criar_tabela = """
    CREATE TABLE IF NOT EXISTS alunos(
        id integer PRIMARY KEY AUTOINCREMENT,
        nome text NOT NULL,
        nota integer NOT NULL
);"""
criar_tabela(conexao, sql_criar_tabela)
# Inserindo alunos
sql_inserir_aluno_felipe = "INSERT INTO alunos (nome, nota) VALUES ('Felipe', 10)"
sql_inserir_aluno_jose = "INSERT INTO alunos (nome, nota) VALUES ('José', 8)"

inserir_aluno(conexao, sql_inserir_aluno_felipe)
inserir_aluno(conexao, sql_inserir_aluno_jose)
# Buscando alunos
sql_buscar_alunos = "SELECT * FROM alunos"
alunos = buscar_alunos(conexao, sql_buscar_alunos)
# Fechando a conexão
fechar_conexao(conexao)
# Mostrando os alunos
for aluno in alunos:
    print(f'O aluno {aluno[1]} tirou nota {aluno[2]}')