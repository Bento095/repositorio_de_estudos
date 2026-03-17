'''
Um banco está desenvolvendo um sistema para caixas eletrônicos e precisa de um programa que simule o saque de dinheiro. O caixa deve entregar o valor solicitado pelo usuário usando a menor quantidade possível de cédulas. As cédulas disponíveis são: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.

Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas de cada tipo serão necessárias para entregar o valor. O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar erros de entrada caso não seja digitado um valor numérico válido. 

'''


def entrada_valor():
    valor = input("Digite o valor do saque (múltiplo de 2): ")
    
    try:
        valor = int(valor)
        if valor % 2 != 0:
            print("Valor inválido. Digite um valor múltiplo de 2.")
        else:
            cedulas = calcular_cedulas(valor)
            print("Cédulas necessárias:")
            for cedula, quantidade in cedulas.items():
                print(f"- R$ {cedula}: {quantidade}")
    except ValueError:
        print("Entrada inválida. Digite um valor numérico válido.")

def calcular_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 2]
    resultado = {}
    
    for cedula in cedulas:
        quantidade = valor // cedula
        if quantidade > 0:
            resultado[cedula] = quantidade
            valor -= quantidade * cedula
            
    return resultado


''' A verção atual do programa é limitada a valores multiplos de 2, mas pode ser facilmente adaptada para incluir outras cédulas ou moedas, caso necessário. O programa também lida com erros de entrada, garantindo que o usuário forneça um valor numérico válido. 

Uma possivel meelhoria seria inplementar um tratamento para ser possivel valores impares ja que dispomos de celulas de 5, ou seja, o programa poderia ser adaptado para aceitar valores impares e calcular as cédulas necessárias para entregar o valor solicitado'''