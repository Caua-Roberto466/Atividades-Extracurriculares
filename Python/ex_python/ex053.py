#Ler uma frase qualquer e dizer se ela é um palíndromo, desconsiderando os espaços. (frase que é igual de trás pra frente desconsiderando os espaços) Ex: a torre da derrota
frase = input("Digite uma frase para saber se ela é um palíndromo: ").lower()
frase_formatada = frase.replace(" ", "")
frase_inversa = ""

for char in frase_formatada:
    frase_inversa = char + frase_inversa

if frase_inversa == frase_formatada:
    print("A frase digitada é um políndromo")
else:
    print("A frase digitada não é um políndromo")