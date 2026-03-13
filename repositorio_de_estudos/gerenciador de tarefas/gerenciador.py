''' Atividae de criar um gerenciador de tarefas, qual permite adicionar, ver e excluir tarefas. O gerenciador deve ser simples e fácil de usar, e deve ser implementado em Python. '''

import os

tarefa = []



def titulo(texto):
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * len(texto))
    print(texto)
    print("=" * len(texto))
    exibir_menu()
    menu()

def  exibir_menu():
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Excluir Tarefa")
    print("4. Sair")

def menu():
    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
            if escolha == 1:
                print("Adicionar Tarefa")
                adicionar_tarefa(tarefa)
            elif escolha == 2:
                print("Ver Tarefas")
                ver_tarefas(tarefa)
            elif escolha == 3:
                print("Excluir Tarefa")
                excluir_tarefa(tarefa)
            elif escolha == 4:
                print("Sair")
                sair()
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    exibir_menu()
    
def ver_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}") 
    acao = input("Pressione Enter para voltar ao menu principal...")
    exibir_menu()

def excluir_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
        exibir_menu()
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
        escolha = input("Digite o número da tarefa que deseja excluir: ")
        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(tarefas):
                tarefa_excluida = tarefas.pop(escolha - 1)
                print(f"Tarefa '{tarefa_excluida}' excluída com sucesso!")
                exibir_menu()
            else:
                print("Número de tarefa inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            exibir_menu()


def sair():
    print("Saindo do Gerenciador de Tarefas. Até logo!")
    exit()