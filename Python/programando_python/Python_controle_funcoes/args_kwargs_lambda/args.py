def media(*notas):
    soma = sum(notas)
    compr = len(notas)
    media = soma / compr
    return media

media1 = media(10, 2)
media2 = media(10, 4, 5, 10)
media3 = media(10, 4, 5, 10, 6, 6)

print(f"{media1:.2f}")
print(f"{media2:.2f}")
print(f"{media3:.2f}")