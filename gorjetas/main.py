from gorjetas import calcular_gorjeta, valor_conta_input, porcentagem_gorjeta_input
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bem-vindo ao calculador de gorjetas!")
    print("Por favor, insira os detalhes da conta para calcular a gorjeta e o total a pagar.")
    valor_conta = valor_conta_input()
    porcentagem_gorjeta = porcentagem_gorjeta_input()
    gorjeta, total_a_pagar = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
    print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
    print(f"Total a pagar: R$ {total_a_pagar:.2f}")

if __name__ == "__main__":
    main()
