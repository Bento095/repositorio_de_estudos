'''
Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.

Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

'''

def identificar_palavras_longas(texto):
    palavras = texto.split()
    palavras_longas = []
    for palavra in palavras:
        if len(palavra) > 10:
            palavras_longas.append(palavra)
    return palavras_longas