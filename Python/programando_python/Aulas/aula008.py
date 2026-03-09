# for c in range(1, 10):
#     print(c)
# print("Fim")

c = 1

while c < 10:
    print(c)
    c+=1

# print("Fim")
# for c in range(1, 5):
#     n = int(input("Digite um valor: "))
# print("Fim")

r = "S"
par = impar = 0
while r == "S":
    a = int(input("Digite um valor: "))
    r = input("Quer continuar? ").upper()

numero = 1
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero != 0:
        if numero % 2 == 0:
            par +=1
        else:
            impar += 1
print(f"Você digitou {par} números pares e {impar} números impares")