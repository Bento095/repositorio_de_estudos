''' Fazer uma calculadora simples usando funções. na base do odio '''

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def sair():
    print("Saindo da calculadora. Até logo!")
    exit()

def calculadora():
    print("Bem-vindo à Calculadora Simples!")
    num1 = float(input("Digite o primeiro número: "))
    print("Escolha a operação (+, -, *, /): ")
    
    print("5. Sair")
    
    escolha = input("Digite o número da operação desejada: ")
    
    if escolha in ['+', '-', '*', '/', '5']:
        num2 = float(input("Digite o segundo número: "))
        
        if escolha == '+':
            print(f"{num1} + {num2} = {somar(num1, num2)}")
        elif escolha == '-':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '*':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '/':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
        elif escolha == '5':
            sair()
    else:
        print("Opção inválida. Por favor, escolha uma operação válida.")