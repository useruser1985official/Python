def soma(num1, num2):
   print(num1 + num2)
def sub(num1, num2):
   print(num1 - num2) 
def div(num1, num2):
   print(num1 / num2)
def mult(num1, num2):
   print(num1 * num2)
def pot(num1, num2):
   print(num1 ** num2)

cont = True

print("Bem-vindo ao Jogo da Matemática!")

while cont == True:
    num1 = int(input("\nDigite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resposta = str(input("\nDigite um operador para começar!\n+)Adição\n-)Subtração\n*)Divisão\n/)Multiplicação\n^)Potenciação\nR: "))
    print("\nResultado:")

    if resposta == "+":
        soma(num1, num2)
    elif resposta == "-":
        sub(num1, num2)
    elif resposta == "*":
        mult(num1, num2)
    elif resposta == "/":
        div(num1,num2)
    elif resposta == "^":
        pot(num1,num2)

    cont2 = input("\nDeseja continuar? [S/N] ")

    if cont2.upper() == "S":
        cont = True
    else:
        cont = False
exit()