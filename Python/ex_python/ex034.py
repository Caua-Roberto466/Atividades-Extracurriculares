salario = float(input("Insira seu salário: R$"))

if salario > 1250:
    aumento = salario+(salario*(10/100))
    print(f'Com o aumento de 10%, o salário que era R${salario}, passou a ser R${aumento}')
else:
    aumento = salario+(salario*(15/100))
    print(f'Com o aumento de 15% o salário que era R${salario}, passou a ser R${aumento}')