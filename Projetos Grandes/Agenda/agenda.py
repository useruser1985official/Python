from os import system, name
from sqlite3 import *

def conectar():
    return connect("dbagenda.db3")

def criar():
    conn = conectar()

    curs = conn.cursor()

    sql = """create table if not exists contato (
    id integer not null primary key,
    nome varchar(50) unique not null,
    email varchar(70) not null,
    telefone varchar(20) not null
)"""

    curs.execute(sql)

def adicionar():
    conn = conectar()

    curs = conn.cursor()

    nome = str(input("Digite seu nome: ")).strip()
    email = str(input("Digite o e-mail: ")).strip()
    telefone = str(input("Digite o telefone: ")).strip()

    sql = "insert into contato (nome, email, telefone) values (?, ?, ?)"

    curs.execute(sql, (nome, email, telefone))

    conn.commit()

    print("\nDados Inseridos com Sucesso!")

def consultar():
    conn = conectar()

    curs = conn.cursor()

    sql = "select * from contato"

    curs.execute(sql)

    print("{:<5} {:<10} {:<20} {:<10}".format("ID", "Nome", "E-mail", "Telefone"))

    print("-" * 50)

    for l in curs.fetchall():
        print("{:<5} {:<10} {:<20} {:<10}".format(l[0], l[1], l[2], l[3]))

    print("")

    conn.close()

def deletar():
    conn = conectar()

    curs = conn.cursor()

    id = str(int(input("Digite a ID do nome a ser excluído: ")))

    sql = "delete from contato where id = ?"

    curs.execute(sql, id)

    conn.commit()

    print("\nContato Excluído com Sucesso!")

    conn.close()

def limpar():
    system("cls" if name == "nt" else "clear")

def opcoes():
    print("=== Agenda Telefônica ===\n")

    print("""1 - Adicionar Contato
2 - Consultar Contatos
3 - Deletar Contato
4 - Sair
""")

    opc = int(input("Digite aqui sua opção: "))

    if opc == 1:
        limpar()
        adicionar()
    elif opc == 2:
        limpar()
        consultar()
    elif opc == 3:
        limpar()
        deletar()
    elif opc == 4:
        limpar()
        print("Saindo...")

        exit()
    else:
        print("Opção Inválida!\n")

    opcoes()

criar()
opcoes()