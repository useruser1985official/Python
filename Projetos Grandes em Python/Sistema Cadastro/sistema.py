from menu.lib.interface import *
from menu.lib.arquivo import *
from time import sleep

arq = "cadastro.txt"

if not arqExiste(arq):
    criarArq(arq)

while True:
    resposta = menu(["Ver Pessoas Cadastradas", "Cadastrar Nova Pessoa", "Sair do Sistema"])

    if resposta == 1:
        # Listar conteudo de arquivo
        lerArq(arq)
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo do Sistema...")
        break
    else:
        print("ERRO! Digite uma Opção Válida!")
    
    sleep(2)