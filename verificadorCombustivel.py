from colorama import init

init()

gasolina = float(input("Digite o preço da gasolina: ").strip().replace(",", "."))
alcool = float(input("Digite o preço do álcool: ").strip().replace(",", "."))

resul = alcool / gasolina

print("")

if resul < 0.7:
    print("\033[32mAbasteça com álcool!\033[m")
else:
    print("\033[31mAbasteça com gasolina!\033[m")
