'''
João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.
'''

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    total_a_pagar = valor_conta + gorjeta
    return gorjeta, total_a_pagar

# Solicita o valor da conta ao usuário
def valor_conta_input():
    while True:
        try:
            valor_conta = float(input("Digite o valor total da conta: R$ "))
            if valor_conta < 0:
                print("Erro: O valor da conta não pode ser negativo. Tente novamente.")
                continue
            return valor_conta
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número válido para o valor da conta.")


def porcentagem_gorjeta_input():
    while True:
        try:
            porcentagem_gorjeta = input("Digite a porcentagem de gorjeta desejada (entre 0 e 100, vazio sera 10%): ")
            if porcentagem_gorjeta == "":
                return 10.0
            porcentagem_gorjeta = float(porcentagem_gorjeta)
            if 0 <= porcentagem_gorjeta <= 100:
                return porcentagem_gorjeta
            else:
                print("Erro: A porcentagem de gorjeta deve estar entre 0 e 100. Tente novamente.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número válido para a porcentagem de gorjeta.")
# Solicita a porcentagem de gorjeta ao usuário


