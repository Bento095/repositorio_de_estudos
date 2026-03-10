'''
Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.

Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial. Exiba a senha gerada.

'''

import os
from gerador_senhas import gerar_senha, tamanho_valido

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    senha = gerar_senha(tamanho_valido())
    print("Senha gerada:", senha)

if __name__ == "__main__":
    main()