ano = int(input("Insira o ano que deseja descobrir se é bissexto ou não "))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("O ano é bissexto")
        else:
            print("O ano não é bissexto")
    else:
        print("O ano é bissexto")
else:
    print("O ano não é bissexto")