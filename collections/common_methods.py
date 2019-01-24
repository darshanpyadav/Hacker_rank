from collections import *

# Counter
if __name__ == "__main__":
    _, seq = input(), input().split()
    seq = Counter(seq)

    total_money = 0

    for i in range(int(input())):
        key, money = input().split()
        if seq[key]:
            seq[key] -= 1
            total_money += int(money)

    print(total_money)


# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
# >>> from collections import Counter
# >>>
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>>
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>>
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]

# -----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    n, m = map(int, input().split())

    seq = defaultdict(list)
    for i in range(n):
        seq[input()].append(str(i + 1))

    inp = []
    for _ in range(m):
        inp.append(input())

    for j in inp:
        if j in seq.keys():
            print(" ".join(seq[j]))
        else:
            print(-1)

# The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict)
# container, but the only difference is that a defaultdict will have a default value if that key has not been set yet.
# If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
# from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print i
#
# ('python', ['awesome', 'language'])
# ('something-else', ['not relevant'])

# -----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    n = int(input())
    order = OrderedDict()

    for _ in range(n):
        item, _, quantity = input().rpartition(" ")
        order[item] = order.get(item) + int(quantity)   # if item in order: #order[item] += int(quantity) # else: #order[item] = int(quantity)

    for j, k in order.items():
        print(j, k)


# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrite
# s an existing entry, the original insertion position is left unchanged.
# >> > ordered_dictionary = OrderedDict()
# >> > ordered_dictionary['a'] = 1
# >> > ordered_dictionary['b'] = 2
# >> > ordered_dictionary['c'] = 3
# >> > ordered_dictionary['d'] = 4
# >> > ordered_dictionary['e'] = 5
# >> >
# >> > print
# ordered_dictionary
# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

# Key takeways
# use of rsplit//rpartition
# use of of get in OrderedDict

# -----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    stu, marks = int(input()), input().split().index("MARKS")
    print(sum([int(input().split()[marks]) for _ in range(stu)]) / stu)


# Basically, namedtuples are easy to create, lightweight object types.
# They turn tuples into convenient containers for simple tasks.
# With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

# >>> from collections import namedtuple
# >>> Point = namedtuple('Point','x,y')
# >>> pt1 = Point(1,2)
# >>> pt2 = Point(3,4)
# >>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
# >>> print dot_product
# 11

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    d = deque()  # initializing result list

    N = int(input())

    for _ in range(N):
        command = input().split()
        if command[0].startswith("pop"):
            eval("d." + command[0] + "()")
        else:
            eval("d." + command[0] + "(" + str(command[1]) + ")")

    print(*list(d))


# A deque is a double-ended queue. It can be used to add or remove elements from both ends.
#
# Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the
# same  performance in either direction.

# Take away
# print(*list) -> used to print space separated list
# ----------------------------------------------------------------------------------------------------------------------
