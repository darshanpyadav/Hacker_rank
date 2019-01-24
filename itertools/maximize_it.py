from itertools import product

if __name__ == "__main__":
    k, m = map(int, input().split())

    elem_arr = (list(map(int, input().split()))[1:] for _ in range(k))
    # creating a generator object

    # take cartesian product of all lists. Find x1**2 + x2**2 + .. for all the combinations
    max_elem = [sum(j ** 2 for j in i) % m for i in product(*elem_arr)]

    print(max(max_elem))


# Take away
# Creation of generator object
# Itertools methods can be used to iterate through the values
# Any function that provides an iterator is a generator function
