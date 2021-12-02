while True:
    entrCpf = str(input("Digite seu CPF: ")).strip()

    strCpf = entrCpf.replace(".", "").replace("-", "")

    if strCpf.isnumeric() and len(strCpf) == 11:
        break

    print("Dados Inválidos Inseridos!")

cont = 0

print("")

while True:
    if cont == 1:
        print("CPF Inválido!")

    prim = int(strCpf[0:1]) * 10
    segu = int(strCpf[1:2]) * 9
    terc = int(strCpf[2:3]) * 8
    quar = int(strCpf[3:4]) * 7
    quin = int(strCpf[4:5]) * 6
    sext = int(strCpf[5:6]) * 5
    seti = int(strCpf[6:7]) * 4
    oita = int(strCpf[7:8]) * 3
    nono = int(strCpf[8:9]) * 2

    tudo = (prim + segu + terc + quar + quin + sext + seti + oita + nono) * 10

    res1 = tudo % 11

    if res1 == 10:
        res1 = 0

    dig1 = int(strCpf[9:10])

    if res1 == dig1:
        verif = True
    else:
        verif = False

    prim = int(strCpf[0:1]) * 11
    segu = int(strCpf[1:2]) * 10
    terc = int(strCpf[2:3]) * 9
    quar = int(strCpf[3:4]) * 8
    quin = int(strCpf[4:5]) * 7
    sext = int(strCpf[5:6]) * 6
    seti = int(strCpf[6:7]) * 5
    oita = int(strCpf[7:8]) * 4
    nono = int(strCpf[8:9]) * 3
    deci = int(strCpf[9:10]) * 2

    tudo = (prim + segu + terc + quar + quin + sext + seti + oita + nono + deci) * 10

    res2 = tudo % 11

    if res2 == 10:
        res2 = 0

    dig2 = int(strCpf[10:11])

    if res2 == dig2:
        verif = True
    else:
        verif = False

    if strCpf == "00000000000" or strCpf == "11111111111" or strCpf == "22222222222" or strCpf == "33333333333" or strCpf == "44444444444" or strCpf == "55555555555" or strCpf == "66666666666" or strCpf == "77777777777" or strCpf == "88888888888" or strCpf == "99999999999":
        verif = False

        print("CPF Inválido!")
        print("Não Coloque o valor \"{}\".".format(entrCpf))

        break

    if verif:
        print("O CPF \"{}\" é válido!".format(entrCpf))

        break
    else:
        if len(entrCpf) == 14:
            valido = entrCpf[0:12]
        else:
            valido = "{}.{}.{}-".format(entrCpf[0:3], entrCpf[3:6], entrCpf[6:9])

        cont += 1

        while True:
            entrCpf = "{}{}{}".format(valido, res1, res2)

            strCpf = entrCpf.replace(".", "").replace("-", "")

            if strCpf.isnumeric() and len(strCpf) == 11:
                break