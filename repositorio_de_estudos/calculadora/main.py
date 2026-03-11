import os
from calculadora import calculadora


def main():
    os.system('cls' if os.name == 'nt' else 'clear' )
    calculadora()   


if __name__ == "__main__":
    main()