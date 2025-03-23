import sqlite3

arquivo_db = 'exp.db'

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
        print('Ops... Deu erro criando a tabela: ', e)

def inserir_dados(conexao, sql_inserir_dado, dados):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql_inserir_dado, dados)
        conexao.commit()
    except sqlite3.Error as e:
        print('Ops... Deu um erro inserindo os dados: ', e)

def atualizar_registro(conexao, matricula, coluna, novo_valor):
    try:
        sql_atualizar = f"""
            UPDATE professor
            SET {coluna} = ?
            WHERE matricula = ?;
        """
        cursor = conexao.cursor()
        cursor.execute(sql_atualizar, (novo_valor, matricula))
        conexao.commit()
        print(f"Registro {matricula} atualizado com sucesso!")
    except sqlite3.Error as e:
        print('Ops... Deu um erro ao atualizar o registro: ', e)

# Iniciando conexão
conexao = iniciar_conexao()

# Criando a tabela professor
sql_criar_tabela = """
    CREATE TABLE IF NOT EXISTS professor(
        matricula integer PRIMARY KEY AUTOINCREMENT,
        nome text NOT NULL,
        disciplina text NOT NULL
    );
"""
criar_tabela(conexao, sql_criar_tabela)

# Entrada de dados para 3 registros
print("Insira os dados de 3 professores:")
for i in range(1, 4):
    nome = input(f'Digite o nome do professor {i}: ')
    disciplina = input(f'Digite a disciplina do professor {i}: ')
    sql_inserir_dado = """
        INSERT INTO professor (nome, disciplina)
        VALUES (?, ?);
    """
    inserir_dados(conexao, sql_inserir_dado, (nome, disciplina))

# Atualizar o registro 2
print("\nVamos atualizar o registro 2:")
coluna = input("Digite a coluna que deseja atualizar (nome ou disciplina): ").strip()
novo_valor = input(f"Digite o novo valor para a coluna {coluna}: ").strip()
atualizar_registro(conexao, 2, coluna, novo_valor)

# Fechar a conexão
fechar_conexao(conexao)
print("Operações concluídas com sucesso!")
