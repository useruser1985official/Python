from datetime import datetime

dia = datetime.now().day
mes = datetime.now().month
ano = datetime.now().year

ds = datetime.now().weekday()

hora = datetime.now().hour
minuto = datetime.now().minute
segundo = datetime.now().second

semana = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo")

print("{:0>2}/{:0>2}/{}".format(dia, mes, ano))
print("{:0>2}:{:0>2}:{:0>2}".format(hora, minuto, segundo))
print(semana[ds])

input("")