# Method that allow us to convert everything to Mayus
text = "This is my text"
results = text.upper()
print(results)

# Method that allow us to convert an index to Mayus
text = "This is my text"
results = text[2].upper()
print(results)

# Method that allow us to convert everything to lowercase
text = "This is my text"
results = text.lower()
print(results)

# Method that allow us to Split the text
text = "This is my text"
results = text.split()
print(results)

# Method that allow us to join split text
a = "Learn"
b = "Python"
c = "is"
d = "cool"
e = " ".join([a,b,c,d])
print(e)

# Method that help us find a character or word in the text
text = "This is my text"
results = text.find("text")
print(results)

# Method that help us find a character or word in the text
text = "This is my text"
results = text.replace("text","replaced_word")
print(results)