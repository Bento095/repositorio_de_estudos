'''
Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.

Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.
'''


def contar_vogais(frase):
    
    vogais = 'aeiou'
    contador = 0
    for char in frase:
        if char in vogais:
            contador += 1
    return contador


