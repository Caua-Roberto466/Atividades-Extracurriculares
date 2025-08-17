print("Formador de triângulos")

l1 = float(input("Insira o primeiro lado de um triângulo "))
l2 = float(input("Insira o segundo lado "))
l3 = float(input("Insira o terceiro "))

if l1 == l2 and l1 == l3:
    print(f'O lados {l1}, {l2}, {l3} formão um triângulo')
    print("O triângulo é equilátero")
else:
    if l1 + l2 > l3 and l1 + l3 > l2 and l3 + l2 > l1:
        print(f'Os lados {l1}, {l2} e {l3} formam um triângulo')
        if l1 == l2 and l1 != l3:
            print("O triângulo é isóceles")
        elif l1 != l2 and l2 != l3:
            print(f'O triângulo é Escaleno')

    else:
        print(f'Os lados {l1}, {l2} e {l3} não formam um triângulo')