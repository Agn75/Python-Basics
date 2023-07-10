# Slice fragments from the String
text = "ABCDEFG"

# As part of the slicing, you need to select the range from the index x to index y
# Take into consideration that y doesn't get included
# text[x : y]
fragment = text[2:5]
print(fragment)

# Print the text in viceversa
fragment = text[:0]
print(fragment)