# Integers, whole numbers
my_number = 1
print(my_number)
[print(type(my_number))]

# Floats, decimal numbers
my_number = 6.4
print(my_number)
[print(type(my_number))]

# Transform a float into an integer
num1 = 5.8
print(type(num1))
num2 = int(num1)
print(type(num2))

# Input results are strings, therefore, we transformed the age into an integer
# then we added 1 to the age on a new variable
age = input("Tell me your age")
age = int(age)
new_age = 1 + age
print(new_age)