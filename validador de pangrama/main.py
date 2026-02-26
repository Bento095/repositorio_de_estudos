'''
Exemplo de pangrama: "The quick brown fox jumps over the lazy dog"
em portugues sem kwy: 'Um pequeno jabuti xereta viu dez cegonhas felizes.'
um com kwy em ptbr: 'Zebras caolhas de Java, pingando whisky e xarope, vêem o gnu quieto.'
e meu favorito: 'todo paje vulgar faz boquinha sexy com kiwi'

'''


import os
from validador_pangramas import eh_pangrama


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    frase = input("Digite uma frase para verificar se é um pangrama: ")
    if eh_pangrama(frase):
        print("A frase é um pangrama!")
    else:
        print("A frase não é um pangrama.")

if __name__ == "__main__":
    main()