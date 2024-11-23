import sqlite3

# Função para criar o banco de dados e a tabela
def criar_banco():
    conn = sqlite3.connect('cupcake_app.db')  # Cria o banco de dados (ou abre se já existir)
    cursor = conn.cursor()
    
    # Cria a tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            endereco TEXT,
            telefone TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Função para adicionar um novo usuário ao banco de dados
def adicionar_usuario(nome, email, endereco, telefone):
    conn = sqlite3.connect('cupcake_app.db')
    cursor = conn.cursor()

    # Insere os dados do usuário na tabela
    cursor.execute('''
        INSERT INTO usuarios (nome, email, endereco, telefone)
        VALUES (?, ?, ?, ?)
    ''', (nome, email, endereco, telefone))

    conn.commit()
    conn.close()

# Chama a função para criar o banco de dados e a tabela
criar_banco()