class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, novo):
        if novo < 1:
            print(f"[ERRO]Valor inválido para depósito! Por favor, deposite um valor acima de 0")
        else:
            self.__saldo += novo
            print(f"Foi depositado {novo} na sua conta, agora você tem {self.__saldo}")
    
class ContaCorrente(ContaBancaria):
    def __init__(self, saldo):
        super().__init__(saldo)
    
    def tipo(self):
        print("Conta Corrente")

class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo):
        super().__init__(saldo)
    
    def tipo(self):
        print("Conta Poupança")

minha_conta = ContaBancaria(saldo=5000)
minha_conta.get_saldo()
print(minha_conta.get_saldo())
minha_conta.depositar(100)

contas = [ContaCorrente(saldo=100), ContaPoupanca(saldo=11)]

for conta in contas:
    conta.tipo()