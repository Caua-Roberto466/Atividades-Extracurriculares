import historico as his
import moedas
from datetime import datetime

def exibir_menu():
    print("")
    print("=-"*21)
    print("Converter moedas")
    print("1 - Converter")
    print("2 - Ver histórico")
    print("3 - Limpar histórico")
    print("0 - Sair")
    print("=-"*21)

def iniciar():
    historico = his.carregar()
    
    while True:
        exibir_menu()
        try:
            escolha = int(input("\nEscola entre 1, 2, 3 ou 0: "))
        except ValueError:
            print("\nDigite um número!")
        else:
            if escolha == 1:
                esc_ori = input("\nQual moeda converter? BRL | USD | EUR | GBP ").upper()
                esc_des = input("Qual o destino da vonversão? 1 - BRL | 2 - USD | 3 - EUR | 4 - GBP ").upper()
                val_conv = float(input("Qual o valor a ser convertido? "))

                try:
                    resultado = moedas.converter(esc_ori, esc_des, val_conv)
                except KeyError:
                    print("\nMoeda inválida, escolha uma da lista")
                else:
                    data = datetime.now().strftime("%d/%m/Y %H:%M")
                    novo_hist = {
                        'Valor': val_conv,
                        'Origem': esc_ori,
                        'Conversão': esc_des,
                        'Resultado': resultado,
                        'Data': data
                    }
                    historico.append(novo_hist)
                    his.salvar(historico)
                    print(f"\nConverção feita, o resultado é {resultado}")

if __name__ == "__main__":
    iniciar()