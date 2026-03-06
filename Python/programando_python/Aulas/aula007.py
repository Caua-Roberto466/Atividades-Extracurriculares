n = int(input("Digite um número "))
passo = int(input("Quantas casas "))
for c in range(0, n+1, passo):
    print(c)
s = 0
limite = int(input("Quantos números será somados"))
for c in range(0, 11):
    n = int(input("Digite um número "))
    s += n
print(f"O somatório é {s}")