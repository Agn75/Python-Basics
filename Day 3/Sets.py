# Set initialization, by using set([x, y, z])
my_set = set([1, 2, 3, 4, 5])
print(type(my_set))
print(my_set)

# Set initialization by using only {x, y, z}
my_set2 = {1, 2, 3, 4, 5}
print(type(my_set))
print(my_set2)

# Union of 2 sets
# sets doesn't repeat numbers, so even after the union, it just keep 1 of each integer
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

# Add more values to the set
set1 = {1, 2, 3, 4, 5}
set1.add(6)
print(set1)

# Remove values from the set
set2 = {1, 2, 3, 4, 5}
set2.remove(3)
print(set2)