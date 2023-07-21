from pathlib import Path

"""
Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.
Recuerda importar Path del módulo pathlib, y utilizar el método home()
"""
ruta_base = Path.home()

"""
Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py"
a partir de la siguiente estructura de carpetas: Curso Python -> Dia 6 -> Practicas_path.py
"""
ruta = Path("Curso Python", "Día 6", "practicas_path.py")

"""
Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a 
partir de la siguiente estructura de carpetas:
"""

ruta = Path(Path.home(), "Curso Python", "Día 6", "practicas_path.py")

# Metodo que me permite hacer una funcion que abra un archivo y lo abra para leer su contenido.
def abrir_leer(archivo):
    archivo = open(archivo)
    return archivo.read()

# Metodo que me permite sobreescribir un archivo por un texto nuevo
def sobrescribir(archivo):
    archivo_sobrescribir = open(archivo, "w")
    archivo_sobrescribir.write("contenido eliminado")

# Metodo que me permite agregar texto al final de un documento sin sobreescribirlo
def registro_error(archivo):
    mi_archivo = open(archivo, "a")
    mi_archivo.write("se ha registrado un error de ejecución")
    mi_archivo.close()