from menu.lib.interface import *

def arqExiste(nome):
    try:
        a = open(nome, "rt") # Abrir pra leitura em modo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArq(nome):
    try:
        a = open(nome, "wt+") # Escrever no arquivo, e cria-lo caso nao exista!
        a.close()
    except:
        print("Houve um erro na criaçao do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")

def lerArq(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabecalho("PESSOAS CADASTRADAS")

        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()

def cadastrar(arq, nome = "desconhecido", idade = 0):
    try:
        a = open(arq, "at")
    except:
        print("Houve um ERRO na abertura dentro do arquivo!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print(f"Novo registro de {nome} adicionado.")
            a.close()