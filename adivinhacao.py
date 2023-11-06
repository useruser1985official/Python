from random import randint
from time import sleep

n = int(randint(1, 9))
p = 0
t = 0

while p != n:
    p = int(input("Digite um número de 1 a 9: "))
    t += 1
    print("Processando...\n")
    sleep(2)
    if p == n:
        print("ACERTOU! Placar {}!".format(t))
    elif p < n:
        print("Chute um valor maior!\n")
    else:
        print("Chute um valor menor!\n")

print("Fim do Jogo!")
