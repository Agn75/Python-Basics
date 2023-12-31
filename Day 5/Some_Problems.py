"""Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio."""


def devolver_distintos(a, b ,c):
    suma = a+b+c
    lista = [a, b, c]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]


print(devolver_distintos(1, 5, 20))

"""
Escribe una función (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d','e','i','n','o','r','t']
"""
def sin_repetir(texto):
    texto_lista = list(set((texto.lower())))
    texto_lista.sort()
    return texto_lista

print(sin_repetir("Hola, como estas?"))

"""
Escribe una función que requiera una cantidad indefinida de argumentos. Lo que hará esta función es devolver True 
si en algún momento se ha ingresado al numero cero repetido dos veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True (6,0,5,1,0,3,0,1) >>> False
"""

def ceros_vecinos(*args):
    contador = 0
    for num in args:
        if contador + 1 == len(args):
            return False
        if args[contador] == 0 and args[contador+1] == 0:
            return True
        else:
            contador += 1
    return False

print(ceros_vecinos(0, 2, 4, 0,  6))


