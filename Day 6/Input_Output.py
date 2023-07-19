# Abrir y leer un archivo
# Tomar en consideracion que el archivo debe encontrarse en la misma carpeta del proyecto
archivo = open("hola.txt")
print(archivo.read())

# Metodo readline() me permite leer unicamente una linea
mi_archivo = open("hola.txt")
print(mi_archivo.readline())

# De esta manera podemos elegir cual linea en especifico leer del archivo
archivo = open("hola.txt")
lineas = archivo.readlines()
print(lineas[1])

# Reemplazar el contenido del archivo
# Siempre se cierra el archivo despues de modificar
archivo = open("hola.txt", "w")
archivo.write("Nuevo texto")
archivo.close()
archivo = open("hola.txt", "r")
print(archivo.read())

# Al final del archivo colocar una nueva linea de texto
archivo = open("hola.txt","a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("hola.txt", "r")
print(archivo.read())

# Poner lineas de separacion por linea agregada
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

registro = open("registro.txt", "a")
for item in registro_ultima_sesion:
    registro.writelines(item + '\t')

registro.close()
registro = open("registro.txt", "r")
print(registro.read())