import sqlite3
from prettytable import PrettyTable

def conectar_banco():
    conn = sqlite3.connect('Cadastro.db')
    return conn

def criar_tabela(conn):
    cursor = conn.cursor()

    # Tabela Cadastro
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cadastro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            endereco TEXT,
            cidade TEXT
        )
    ''')

    conn.commit()

def cadastrar_dados_interativamente(conn):
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    endereco = input("Informe o endereço: ")
    cidade = input("Informe a cidade: ")

    cursor = conn.cursor()
    cursor.execute("INSERT INTO Cadastro (nome, idade, endereco, cidade) VALUES (?, ?, ?, ?)", (nome, idade, endereco, cidade))
    conn.commit()
    print("Cadastro realizado com sucesso!")

def consultar_dados(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cadastro")

    # Criar uma tabela formatada para exibição
    tabela = PrettyTable()
    tabela.field_names = ["ID", "Nome", "Idade", "Endereço", "Cidade"]

    # Adicionar os dados à tabela
    for row in cursor.fetchall():
        tabela.add_row(row)

    # Exibir a tabela
    print("\n### Dados Cadastrados ###")
    print(tabela)

def main():
    conn = conectar_banco()
    criar_tabela(conn)

    while True:
        opcao = input("\nEscolha uma opção:\n1. Cadastrar Dados\n2. Consultar Dados\n3. Sair\nOpção: ")

        if opcao == '1':
            cadastrar_dados_interativamente(conn)
        elif opcao == '2':
            consultar_dados(conn)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    conn.close()

if __name__ == "__main__":
    main()