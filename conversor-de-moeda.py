cot = float(input("Digite a cotação de US$ 1,00 em R$: "))
val = float(input("\nDigite um valor em R$: "))
dol = val / cot
print("Você tem R${:.2f} e pode comprar US${:.2f}.".format(val, dol))