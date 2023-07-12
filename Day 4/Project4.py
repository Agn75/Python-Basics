# Importing Random library
from random import *
# Program asks for the player's name
nombre_jugador = input("Ingresa tu nombre: ")
intentos = 0
numero_maquina = randint(1, 100)

# Game responds to the player and explains the game
print(f"Bueno {nombre_jugador}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cual es")

while intentos < 8:
    intentos = intentos+1
    numero = int(input("Por favor, escoge un numero: "))
    if numero < 1 or numero > 100:
        print("Número no permitido")
        continue
    elif numero < numero_maquina:
        print("Respuesta incorrecta, ha elegido un número menor al número secreto")
        continue
    elif numero > numero_maquina:
        print("Respuesta incorrecta, ha elegido un número mayor al número secreto")
        continue
    elif numero == numero_maquina:
        print(f"Has ganado! Acertaste el número secreto! Te ha tomado {intentos} intentos!")
        break

if numero != numero_maquina:
    print(f"Perdiste! El número secreto era {numero_maquina}")
