from contar_vogais import contar_vogais
import os



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    frase = input("Digite um texto: ").strip()
    if not frase:
        print("Erro: Nenhum texto foi digitado.")
    else:
        resultado = contar_vogais(frase)
        print(f"O texto contém {resultado} vogais.")

if __name__ == "__main__":
    main()