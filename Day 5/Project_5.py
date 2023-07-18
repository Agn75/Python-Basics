import random
from random import *

lista_palabras = ["Alfredo", "Esteban", "Kattia", "Felipe", "Victoria"]

def elegir_palabra(lista):
    palabra_escogida = choice(lista)
    palabra_desglozada= list(palabra_escogida)
    print(palabra_desglozada)
    return palabra_desglozada


def verificar_letra(palabra):
    contador = 0
    letra = input("Ingresar Letra deseada: ")
    for letra in palabra:
        if letra != palabra[contador]:
            contador += contador
        else:
            print("La letra esta en la palabra!")




verificar_letra(elegir_palabra(lista_palabras))