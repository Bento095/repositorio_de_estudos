"""Validador de pangramas

Um pangrama é uma frase que contém todas as letras do alfabeto."""


def eh_pangrama(frase):
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    letras_frase = set(frase.lower())
    return alfabeto.issubset(letras_frase)