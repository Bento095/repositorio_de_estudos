from static.visual import exibir_titulo, sair
from numero_secreto import jogar, menu
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear' )
    exibir_titulo()
    menu()
    jogar()

if __name__ == "__main__":
    main()