import sqlite3

# Conectar ao Banco de Dados
def conectarBancoDeDados():
    return sqlite3.connect('database.db')

# Criar uma Tabela
def criarTabela():
    conexao = conectarBancoDeDados()

    conexao.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            cpf TEXT PRIMARY KEY NOT NULL,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            curso TEXT,
            matricula INTEGER NOT NULL,
            turma TEXT,
            fone TEXT NOT NULL,
            endereco TEXT NOT NULL,
            data_nascimento TEXT,
            email TEXT NOT NULL
        )
    ''')
    
    conexao.close()

# Inserir um registro na tabela
def inserirRegistro(nome, idade, curso, matricula, cpf, turma, fone, endereco, data_nascimento, email):
    conexao = conectarBancoDeDados()
    
    conexao.execute('''
        INSERT INTO alunos(nome, idade, curso, matricula, cpf, turma, fone, endereco, data_nascimento, email)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nome, idade, curso, matricula, cpf, turma, fone, endereco, data_nascimento, email)) 
    # Salvar as alterações no Banco de Dados
    conexao.commit()
    conexao.close()

# Recuperar todos os registros da Tabela
def listarAlunos():
    conexao = conectarBancoDeDados()
    resultado = conexao.execute('SELECT * FROM alunos')
    # Iterar sobre os resultados
    for row in resultado:
        print('''{}, {} anos
            Matrícula: {}
            CPF: {}
            Fone: {}
            Curso: {}
            Turma: {}
            Endereço: {}
            Data de Nascimento: {}
            Email: {}'''.format(row[1], row[2], row[4], row[0], row[6], row[3], row[5], row[7], row[8], row[9]))
    conexao.close()

# Deletar aluno
def deletarAluno(pk):
    conexao = conectarBancoDeDados()

    conexao.execute('DELETE FROM alunos WHERE cpf = ?', (pk,))
    conexao.commit()

    conexao.close()

# Atualizar dados de um aluno
def atualizarAluno(cpf, nome=None, idade=None, curso=None, matricula=None, turma=None, fone=None, endereco=None, data_nascimento=None, email=None):
    conexao = conectarBancoDeDados()

    # Construir a query dinamicamente com os parâmetros passados
    query = "UPDATE alunos SET"
    params = []

    if nome:
        query += " nome = ?,"
        params.append(nome)
    if idade:
        query += " idade = ?,"
        params.append(idade)
    if curso:
        query += " curso = ?,"
        params.append(curso)
    if matricula:
        query += " matricula = ?,"
        params.append(matricula)
    if turma:
        query += " turma = ?,"
        params.append(turma)
    if fone:
        query += " fone = ?,"
        params.append(fone)
    if endereco:
        query += " endereco = ?,"
        params.append(endereco)
    if data_nascimento:
        query += " data_nascimento = ?,"
        params.append(data_nascimento)
    if email:
        query += " email = ?,"
        params.append(email)

    # Remover a vírgula final e adicionar o WHERE para garantir que o cpf seja único
    query = query.rstrip(',') + " WHERE cpf = ?"
    params.append(cpf)

    # Executar a query
    conexao.execute(query, tuple(params))
    
    # Salvar as alterações no Banco de Dados
    conexao.commit()
    conexao.close()

    print('Dados do aluno com CPF {} atualizados com sucesso.'.format(cpf))

criarTabela()
inserirRegistro('Henrique Prates Cardoso', 19, 'Sistemas para Internet', 201012600055, '555.555.555.00', 'B', '61998832328', 'Rua A, Bairro B, Lote C, Casa D', '05-03-2005', 'henrique.cardoso@mail.com')
inserirRegistro('Ana Prates Cardoso', 29, 'Sistemas para Internet', 221012600055, '222.222.222.55', 'B', '619988322428', 'Rua A, Bairro B, Lote C, Casa D', '05-08-2005', 'ana.cardoso@mail.com')
inserirRegistro('Caroline Prates Cardoso', 14, 'Eventos', 251012600055, '777.777.777.11', 'D', '61998832329', 'Rua A, Bairro B, Lote C, Casa D', '05-03-2010', 'caroline.cardoso@mail.com')
listarAlunos()
deletarAluno('777.777.777.11')
atualizarAluno('555.555.555.00', 'Henrique Prates Inácio')