def limpar_texto(frase):
    texto = texto.lower()
    caracteres = "!@#$%^&*()_+-=~`[]{}|;:'\",.<>/?"
    for char in caracteres:
        texto = texto.replace(char, "")
    return texto

def contar_palavras(frase):
    palavras = frase.split()
    print(len(palavras))
    return len(palavras)


def contar_palavras(frase):
    frase = limpar_texto(frase)
    if not frase.strip():
        return {}
    palavras = frase.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
        return contagem