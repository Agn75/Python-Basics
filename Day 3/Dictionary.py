dictionary = {'c1':"valor1", 'c2':"valor1"}
print(dictionary)

results = dictionary['c1']
print(results)

client = {"client_firstname": "Juan", "client_lastname": "Fuentes", "client_weight": 88}
query = client["client_firstname"]
print(query)

# Exercise to print what c2 has and show it in uppercase
dic = {"c1": ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic['c2'][1].upper())

# Add a new value to the dictionary
dic2 = {1: "a", 2: "b"}
dic2[3] = "c"
print(dic2)

# Command that shows all the dictionary keys
print(dic2.keys())

# Command that shows all the the dictionary values
print(dic2.values())

