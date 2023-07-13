from random import *

# Lista inicial
palitos = ['-', '--', '---', '----']


# mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# Pedir el intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)


# Comprobar intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("Has perdido")
    else:
        print("Ganaste!")
    print(f"Te ha tocado {lista[intento - 1]}")

# Checking results
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)


# Method that will throw a dice with a value from 1 to 6.
def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2


# Method that evaluates the dice results and make operations out of it.
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 10 > suma_dados > 6:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# Checking results
resultado_dados = lanzar_dados()
mensaje = evaluar_jugada(resultado_dados[0],resultado_dados[1])
print(mensaje)

