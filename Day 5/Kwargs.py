"""
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan,
y devuelva esa cantidad como resultado.
"""

def cantidad_atributos(**kwargs):
    return len(kwargs)

resultado = cantidad_atributos(nombre="juan", edad =25, ciudad="Madrid")
print(resultado)

def lista_atributos(**kwargs):
    return [kwargs.values()]

resultado2 = lista_atributos(nombre="Juan", edad=25, ciudad="Madrid")
print(resultado2)