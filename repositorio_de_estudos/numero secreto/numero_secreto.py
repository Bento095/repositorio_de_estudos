import random

from static.visual import exibir_titulo, sair, exibir_opcoes

def jogar():
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    while True:
        try:
            chute = int(input("Digite um número entre 1 e 100: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue
        
        tentativas += 1
        
        if chute < numero_secreto:
            print("O número secreto é maior. Tente novamente.")
        elif chute > numero_secreto:
            print("O número secreto é menor. Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas!")
            sair()


def menu():
    numero = exibir_opcoes()
    match numero:
        case "1":
            jogar()
        case "2":
            sair()
        case _:
            print("Opção inválida. Tente novamente.")
            return menu()