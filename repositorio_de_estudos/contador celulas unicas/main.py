import os
from caixa_eletronico import calcular_cedulas, entrada_valor


def main():
    texto = "Contador de Células Únicas"
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * len(texto))
    print(texto)
    print("=" * len(texto))
    entrada_valor()

if __name__ == "__main__":
    main()