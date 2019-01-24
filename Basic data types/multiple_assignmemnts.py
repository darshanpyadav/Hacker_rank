# Multiple assignments can be made in a single line

x, y = 10, 20
# x, y = (10, 20)
# (x, y) = 10, 20
# (x, y) = (10, 20)

# Multiple assignment is called tuple unpacking

# you can use tuple unpacking even in for loops
person_dictionary = {"a": 1, "b": 2}
for key, value in person_dictionary.items():
    print(f"Key {key} has value {value}")

# using *var to take the rest of the variables

# >>> numbers = [1, 2, 3, 4, 5, 6]
# >>> first, *rest = numbers
# >>> rest
# [2, 3, 4, 5, 6]
# >>> first
# 1