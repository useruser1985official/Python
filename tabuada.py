num = int(input("Digite um número para ver sua tabuada: "))
print("\nTabuada de {}:\n".format(num))
print("-" * 13)
for t in range(1, 10 + 1):
    print("{} x {} = {}".format(num, t, num * t))
print("-" * 13)