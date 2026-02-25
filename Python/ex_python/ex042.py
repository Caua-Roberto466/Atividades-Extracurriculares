l1 = float(input("Insira o primeiro valor: "))
l2 = float(input("Insira o segundo médio: "))
l3 = float(input("Insira o terceiro valor: "))
cores = {'limpa':'\033[m' ,'ciano' : '\033[36m', 'vermelho' : '\033[31m'}

if l1 < l2 + l3 and l2 <l1 + l3 and l3< l2 + l1:
    print(f'Os lados {cores["ciano"]}{l1}{cores["limpa"]}, {cores["ciano"]}{l2}{cores["limpa"]} e {cores['ciano']}{l3}{cores["limpa"]} podem formar um tirângulo')
    if l1 == l2 ==l3 :
        print(f'Os lados {cores["ciano"]}{l1}{cores["limpa"]}, {cores["ciano"]}{l2}{cores["limpa"]} e {cores["ciano"]}{l3}{cores["limpa"]} formam um triângulo equilátero')
    elif l1 == l2  and l3 != l2 or l3 == l2 and l3 != l1 or l1 ==l3 and l3 != l2:
        print(f'Os lados {cores["ciano"]}{l1}{cores["limpa"]}, {cores["ciano"]}{l2}{cores["limpa"]} e {cores['ciano']}{l3}{cores["limpa"]} formam um triângulo isóceles')
    else:
        print(f'Os lados {cores["ciano"]}{l1}{cores["limpa"]}, {cores["ciano"]}{l2}{cores["limpa"]} e {cores["ciano"]}{l3}{cores["limpa"]} formam um triângulo escaleno')
else:
    print(f'Com os valores inserido {cores["vermelho"]}não se forma o tirângulo{cores['limpa']}')
