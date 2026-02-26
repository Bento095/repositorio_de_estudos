import secrets
import string

def tamanho_valido():
    try:
        tamanho = int(input("Digite o tamanho da senha (12 caracteres recomendados): ").strip() or "12")
    except ValueError:
        print("Entrada inválida. Usando tamanho padrão de 12 caracteres.")
        tamanho = 12

    return tamanho


def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))

    return senha