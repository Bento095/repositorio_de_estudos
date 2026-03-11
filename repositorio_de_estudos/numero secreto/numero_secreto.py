'''
Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.

Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.

Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .

'''

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