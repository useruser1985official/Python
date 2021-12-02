import sys
import dns.resolver
import colorama

colorama.init()

try:
    dominio = str(input("Insira o nome ou IP do domínio: "))
except:
    print("O domínio é inválido!")
    sys.exit(1)

try:
    arquivo = open("wordlist.txt")
    linhas = arquivo.read().splitlines()
except:
    print("Arquivo não encontrado ou inválido!")
    sys.exit(1)

print("-=" * 30)

for l in linhas:
    subdominio = l + "." + dominio

    try:
        respostas = dns.resolver.resolve(subdominio, "a")

        for res in respostas:
            print("\033[32m{}\033[m - \033[34m{}\033[m".format(subdominio, res))
    except:
        pass

print("Scanner Concluído!")
print("-=" * 30)
