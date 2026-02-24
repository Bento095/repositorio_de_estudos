from validador import validar_cpf
import os


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    cpf = input("Digite seu CPF: ").strip()
    if validar_cpf(cpf):
        print("CPF válido!")
    else:
        print("CPF inválido!")

if __name__ == "__main__":
    main()