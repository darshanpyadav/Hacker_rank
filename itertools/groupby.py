from itertools import *

if __name__ == "__main__":
    # string = input()

    # for i, j in groupby(string):
    #     print("(" + str(len(list(j))) + ", " + str(i) + ")", end=" ")
    print(*[(len(list(c)), int(k)) for k, c in groupby(input())])


# Take away

# groupby takes an iterable and breaks at the change (whenever i != i+1)
# groupby returns a key value pair
# key is the item at which it broke
# value is an iterator with all the vales of the key


# Usage of * i.e args
# a, *b = 1, 2, 3, 4, 5

# a
# Out[26]: 1

# b
# Out[27]: [2, 3, 4, 5]

# print(b)
# [2, 3, 4, 5]

# print(*b)
# 2 3 4 5
