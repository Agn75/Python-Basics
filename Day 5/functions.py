def saludar_persona(nombre):
    print("Hola " + nombre)

saludar_persona("Fernando")

nombre_persona = "Alfredo"
def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")

bienvenida(nombre_persona)

un_numero = 3

def cuadrado(un_numero):
    numero_cuadrado = un_numero**2
    print(f"El cuadrado del numero dado es {numero_cuadrado}")

cuadrado(un_numero)

Palabra = "hola"
def invertir_palabra(palabra):
    resultado = palabra[::-1]
    resultado_mayus = resultado.upper()
    print(resultado_mayus)
    return resultado_mayus

invertir_palabra(Palabra)

lista_numeros = [2, 4, 6, -1, -4]


def todos_positivos(lista_numeros):
    for x in lista_numeros:
        if x > 0:
            return True
        else:
            pass
    return False

todos_positivos(lista_numeros)

lista_numeros2 = [1, 4, 2, 123, 5123, 62134]
def suma_menores(lista_numeros2):
    suma = 0
    for x in lista_numeros2:
        if 0 < x < 1000:
            suma = x + suma
    return suma

suma_menores(lista_numeros2)