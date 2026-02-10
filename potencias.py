num = int(input("Digite um número para ver suas potências: "))
print("\nPotências de {}:\n".format(num))
print("-" * 40)
for t in range(0, 20 + 1):
    print("{} ^ {} = {}".format(num, t, num ** t))
print("-" * 40)
