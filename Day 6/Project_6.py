import os
from pathlib import Path
from os import system

# Inicializacion de la ruta donde se encuentran las carpetas que creamos
mi_ruta = Path(Path.home(), 'Recetas')

# Mostrar Menu de inicio
def inicio():
    while True:
        try:
            system('clear')  # Se utiliza para limpiar la pantalla.
            print('Bienvenido al administrador de recetas')
            print(f'La cantidad de recetas que se encuentran en la ruta: {mi_ruta} es de: {contar_recetas(mi_ruta)}')
            print('*' * 6)
            print("Estan son las opciones disponibles:")
            print("""
            [1] - Leer receta
            [2] - Crear receta
            [3] - Crear categoria nueva
            [4] - Eliminar receta
            [5] - Eliminar Categoria
            [6] - Salir
            """)
            eleccion_usuario = input("Elige una opcion: ")

            # Comprobar si la elección es un número válido
            if eleccion_usuario.isdigit():
                eleccion_usuario = int(eleccion_usuario)
                if 1 <= eleccion_usuario <= 6:
                    return eleccion_usuario
                else:
                    print("Elegiste un valor incorrecto! Por favor, elige una opción válida (1 a 6).")
            else:
                print("Elegiste un valor incorrecto! Por favor, ingresa un número.")
        except ValueError:
            print("Elegiste un valor incorrecto! Por favor, ingresa un número válido.")


# Metodo que nos permite contar cuantos files de tipo txt hay en la ruta que otorgamos usando el metodo glob
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob('**/*.txt'):
        contador += 1
    return contador

def mostrar_categorias(ruta):
    print("Categorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'[{contador}] - {carpeta_str}')
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista)+1):
        eleccion_correcta = input("\nElije una categoria: ")
    return lista[int(eleccion_correcta) -1]

def mostrar_recetas(ruta):
    print("Recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 0

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f'[{contador}] - {receta_str}')
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

def elegir_receta(lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) +1):
        eleccion_receta = input('\nElige una receta: ')
    return lista[int(eleccion_receta) - 1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)
        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada!")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")

def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu Nueva categoria: {nombre_categoria} ha sido creada!")
            existe = True
        else:
            print("Lo siento, esa categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print("La receta ha sido eliminada!")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print("La Categoria ha sido eliminada")

def volver_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V para volver al menu: ")

def operacion_switch(numero_escogido):
    while True:
        match numero_escogido:
            case 1:
                mis_categorias = mostrar_categorias(mi_ruta)
                mi_categoria = elegir_categoria(mis_categorias)
                mis_recetas = mostrar_recetas(mi_categoria)
                mi_receta = elegir_receta(mis_recetas)
                leer_receta(mi_receta)
                volver_inicio()
            case 2:
                mis_categorias = mostrar_categorias(mi_ruta)
                mi_categoria = elegir_categoria(mis_categorias)
                crear_receta(mi_categoria)
                volver_inicio()
            case 3:
                crear_categoria(mi_ruta)
                volver_inicio()
            case 4:
                mis_categorias = mostrar_categorias(mi_ruta)
                mi_categoria = elegir_categoria(mis_categorias)
                mis_recetas = mostrar_recetas(mi_categoria)
                mi_receta = elegir_receta(mis_recetas)
                eliminar_receta(mi_receta)
                volver_inicio()
            case 5:
                mis_categorias = mostrar_categorias(mi_ruta)
                mi_categoria = elegir_categoria(mis_categorias)
                elegir_categoria(mi_categoria)
                volver_inicio()
            case 6:
                return False
            case _:
                print("Elegiste un valor incorrecto!")
                numero_escogido == inicio()


operacion_switch(inicio())