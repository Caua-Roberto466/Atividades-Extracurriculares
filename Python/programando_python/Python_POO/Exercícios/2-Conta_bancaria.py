class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def sacar(self, valor):
        if valor < 1:
            raise ValueError("Não é possível sacar saldo abaixo de R$1")
        elif valor > self.__saldo:
            raise ValueError("Saldo insuficiente")
        else:
            self.__saldo -= valor
    
    def depositar(self, valor):
        if valor < 1:
            raise ValueError("Digite um número maior que 0")
        else:
            self.__saldo += valor
    
conta = ContaBancaria(saldo=100)

try:
    valor = int(input("Insira o valor do saque "))
    conta.sacar(valor)
except ValueError as e:
    print(f"[ERRO] {e}")
else:
    print(conta.get_saldo())
finally:
    print("Operação realizado")