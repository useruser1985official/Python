from random import randint
from time import sleep

jog = ""
comp = ""

while jog == comp:
    num = randint(1, 3)

    if num == 1:
        comp = "Pedra"
    elif num == 2:
        comp = "Papel"
    elif num == 3:
        comp = "Tesoura"

    print("Vamos jogar Jokenpô, escolha uma opção.")

    print("\n1 - Pedra\n2 - Papel\n3 - Tesoura\n")

    opc = int(input("Digite sua opção: "))

    if opc == 1:
        jog = "Pedra"
    elif opc == 2:
        jog = "Papel"
    elif opc == 3:
        jog = "Tesoura"
    else:
        print("Opção Inválida!")
        exit()

    print("\nJO")
    sleep(0.75)
    print("KEN")
    sleep(0.75)
    print("PÔ")

    if jog == "Pedra" and comp == "Papel":
        print("\nInfelizmente você perdeu.\nComputador escolheu {} e você escolheu {}.\nPapel embrulha Pedra!".format(comp, jog))
    elif jog == "Papel" and comp == "Tesoura":
        print("\nInfelizmente você perdeu.\nComputador escolheu {} e você escolheu {}.\nTesoura corta Papel!".format(comp, jog))
    elif jog == "Tesoura" and comp == "Pedra":
        print("\nInfelizmente você perdeu.\nComputador escolheu {} e você escolheu {}.\nPedra quebra Tesoura!".format(comp, jog))
    elif jog == "Pedra" and comp == "Tesoura":
        print("\nParabéns, você venceu!\nComputador escolheu {} e você escolheu {}.\nPedra quebra Tesoura!".format(comp, jog))
    elif jog == "Tesoura" and comp == "Papel":
        print("\nParabéns, você venceu!\nComputador escolheu {} e você escolheu {}.\nTesoura corta Papel!".format(comp, jog))
    elif jog == "Papel" and comp == "Pedra":
        print("\nParabéns, você venceu!\nComputador escolheu {} e você escolheu {}.\nPapel embrulha Pedra!".format(comp, jog))
    else:
        print("\nO computador escolheu {} e você também escolheu {}.\nReiniciando...\n".format(comp, jog))
        sleep(3)