# Method to import libraries
from random import *

# Methos that picks a random number from the parameter range
rand = randint(1, 50)
print(rand)

# Uniform will allow us to send a float random number
rand2 = uniform(1, 50)
print(rand2)

# random() choose anything between 0 and 1
rand3 = random()
print(rand3)

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [x for x in valores if x%2 == 0]
print(valores_pares)

