# Input to request the text to analyze
poem = input("Please Type a Poem to analyze: ").lower()

# Input to ask for 3 random characters to find in the text
char1 = input("Please Type 1 random character: ").lower()
char2 = input("Please type a second character: ").lower()
char3 = input("Please type a third random character: ").lower()

# Adding the 3 words into a list for manipulation
list_char = [char1, char2, char3]

# Count method to find how many times the characters appear on the text
number_char1 = poem.count(char1)
number_char2 = poem.count(char2)
number_char3 = poem.count(char3)

# Printing the times that the characters appear on the text
print(f"(We found the letter {char1} repeated {number_char1} times)")
print(f"(We found the letter {char2} repeated {number_char2} times)")
print(f"(We found the letter {char3} repeated {number_char3} times)")

# Splitting the text into words and running a len command to count them
words_count = poem.split()
words_count = len(words_count)

# Printing the number of words in the text
print(f"The number of words in the text given is: {words_count}")

# Obtaining which is the 1st and last character on the text
first_char = poem[0]
last_char = poem[-1]

# Printing the 1st and last characters
print(f"The first character of the text is: {first_char} and the last character is: {last_char}")

# reversing the poem letters
reverse_text = poem[::-1]

# printing the reversed text
print(f"The reverse text is: {reverse_text}")

# Looks for an specific word on the text
search_word = "python" in poem
dic = {True:"Yes", False:"No"}

# Printing the results of searching a word
print(f"Is the word Python in the text? {dic[search_word]}")