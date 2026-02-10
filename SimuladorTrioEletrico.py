from random import choice
from time import sleep
from rich import print

posicao = 0
distanciaTotal = 100
velocidade = 0
seguranca = 100
paciencia = 100

print(":notes: :drum: :guitar: :loud_sound: TRIO ELÉTRICO SIMULATOR :loud_sound: :guitar: :drum: :notes:")
print("Chegue ao fim do circuito sem causar o caos.")

while posicao < distanciaTotal and seguranca > 0 and paciencia > 0:
    print(f"\n:busstop: Posição: {posicao}/100")
    print(f":truck: Velocidade: {velocidade} Km/h")
    print(f":stop_sign: Segurança: {seguranca}")
    print(f":brain: Paciência: {paciencia}")

    acao = input("\nAções: [A]celerar/[F]rear/[M]anter: ").lower()[0]

    if acao == "a":
        velocidade += 1
    elif acao == "f":
        velocidade = max(0, velocidade - 1)

    # Eventos aleatórios:

    evento = choice(("nada", "foliao", "poste", "artista"))

    if evento == "foliao" and velocidade > 2:
        print(":scream: Folião apareceu na frente!")
        seguranca -= 20
    elif evento == "poste" and velocidade > 1:
        print(":high_voltage: Poste e fiação perigosamente próximos!")
        seguranca -= 10
    elif evento == "artista" and velocidade > 0:
        print(":microphone: Artista mandou parar AGORA!")
        paciencia -= 10
        velocidade = 0

    posicao += velocidade
    paciencia -= 1

    sleep(1)

# Fim de jogo
if seguranca <= 0:
    print("\n:collision: CAOS TOTAL! Trio interditado!")
elif paciencia <= 0:
    print("\n:dizzy_face: Motorista surtou! Fim de jogo!")
else:
    print("\n:party_popper: SUCESSO! Trio chegou ao fim do circuito!")
