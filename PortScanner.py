import socket

serv = str(input("Coloque o link ou IP no site: "))

print("-=" * 30)

for p in range(1, 65536):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.5)
    codigo = cliente.connect_ex((serv, p))

    if codigo == 0:
        print("A porta {} do servidor {} está aberta.".format(p, serv))

print("Scanner de Portas Concluído!")

print("-=" * 30)