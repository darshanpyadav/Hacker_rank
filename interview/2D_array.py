from itertools import product

arr = []
sum_max = float("-inf")

for i in range(6):
    arr.append(list(map(int, input().split())))

elem_list = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)]

for i, j in product(range(4), range(4)):
    s = 0
    for a1, a2 in elem_list:
        s += arr[a1 + i][a2 + j]
    if s > sum_max:
        sum_max = s

print(sum_max)

# Order 0(n)