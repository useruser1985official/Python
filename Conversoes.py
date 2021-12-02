import os

cont = "S"

while cont in "Ss":
    os.system("cls" if os.name == "nt" else "clear")
    numero = int(input("Digite um número inteiro decimal qualquer: "))

    if numero >= 0:
        print("\nO número {} em binário é {}.".format(numero, bin(numero)[2:]))
        print("O número {} em octal é {}.".format(numero, oct(numero)[2:]))
        print("O número {} em hexadecimal é {}.".format(numero, hex(numero).upper()[2:]))
    else:
        print("\nERRO: Número negativo não pode ser convertido!")

    cont = str(input("\nDeseja verificar outro número? [S/N] ")).strip().upper()[0]
