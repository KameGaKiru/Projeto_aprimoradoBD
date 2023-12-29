import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('Projeto_aprimorado.db')

# Criar as tabelas
conn.execute('''
    CREATE TABLE IF NOT EXISTS Pessoa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        endereco TEXT
    )
''')

conn.execute('''
    CREATE TABLE IF NOT EXISTS Cidade (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
''')

conn.execute('''
    CREATE TABLE IF NOT EXISTS Registro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pessoa_id INTEGER,
        cidade_id INTEGER,
        FOREIGN KEY (pessoa_id) REFERENCES Pessoa (id),
        FOREIGN KEY (cidade_id) REFERENCES Cidade (id)
    )
''')

# Inserir dados
conn.execute("INSERT INTO Pessoa (nome, idade, endereco) VALUES ('Joao', 25, 'Liberdade')")
conn.execute("INSERT INTO Pessoa (nome, idade, endereco) VALUES ('Maria', 30, 'Estácio')")
conn.execute("INSERT INTO Pessoa (nome, idade, endereco) VALUES ('Wadje', 23, 'Travessa Jaguarão')")
conn.execute("INSERT INTO Pessoa (nome, idade, endereco) VALUES ('Regina', 60, 'Travessa Rondonópolis')")

conn.execute("INSERT INTO Cidade (nome) VALUES ('São Paulo')")
conn.execute("INSERT INTO Cidade (nome) VALUES ('Rio de Janeiro')")
conn.execute("INSERT INTO Cidade (nome) VALUES ('Recife')")
conn.execute("INSERT INTO Cidade (nome) VALUES ('Tambaú')")

conn.execute("INSERT INTO Registro (pessoa_id, cidade_id) VALUES (1, 1)")
conn.execute("INSERT INTO Registro (pessoa_id, cidade_id) VALUES (2, 2)")
conn.execute("INSERT INTO Registro (pessoa_id, cidade_id) VALUES (3, 3)")
conn.execute("INSERT INTO Registro (pessoa_id, cidade_id) VALUES (4, 4)")

# Consulta usando INNER JOIN
cursor = conn.execute('''
    SELECT Pessoa.nome, Pessoa.idade, Cidade.nome
    FROM Pessoa
    INNER JOIN Registro ON Pessoa.id = Registro.pessoa_id
    INNER JOIN Cidade ON Registro.cidade_id = Cidade.id
''')

for row in cursor:
    print(f'Nome: {row[0]}, Idade: {row[1]}, Cidade: {row[2]}')

# Fechar a conexão
conn.close()