frase = str(input("Digite uma frase: ")).strip().upper()
pal = frase.split()
junt = "".join(pal)
inv = ""
for let in range(len(junt) - 1, -1, -1):
    inv += junt[let]
print("O inverso de {} é {}.".format(junt, inv))
if inv == junt:
    print("Temos um palíndromo!")
else:
    print("Não é palíndromo!")