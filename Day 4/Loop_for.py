# For loop can be used only on iterable variables such as lists and directories
names = ["Alfredo", "Esteban", "Kattia"]

# For loop that will go thru the list of names and display one by one showing its current position on the list
for list_name in names:
    num_name = names.index(list_name)
    print("Name: " + list_name + f" which is located in the position {num_name}")

# List of numbers and a new integer variable
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_numeros = 0

# For loop that adds + every object in the list
for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
print(suma_numeros)

suma_pares = 0
suma_impares = 0
# For lopp that shows the results of + pairs and non-pairs
for num in lista_numeros:
    if num%2 == 0:
        suma_pares = suma_pares + num
    else:
        suma_impares = suma_impares + num
print(f"La suma de los numeros pares es: {suma_pares}, mientras que la suma de los impares es: {suma_impares}")