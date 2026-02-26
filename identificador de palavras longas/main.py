import os
from identificar_palavras import identificar_palavras_longas

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    texto = input('Digite o texto: ')
    palavras_longas = identificar_palavras_longas(texto)
    if palavras_longas:
        print(f"Palavras longas encontradas: {', '.join(palavras_longas)}")
    else:
        print("Nenhuma palavra longa foi encontrada no texto.")

if __name__ == "__main__":
    main()