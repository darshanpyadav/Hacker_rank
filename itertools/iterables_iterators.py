from itertools import combinations
from time import time

if __name__ == "__main__":
    _, string, r = int(input()), input().split(), int(input())

    start = time()
    total_count = list(combinations(string, r))
    count = [1 for i in total_count if 'a' in i]
    # count = list(filter(lambda c: 'a' in c, total_count))

    # f'{value:{width}.{precision}}'
    print(f'{len(count)/len(total_count):.4f}')
    print(f'{time() - start:4f}')


# Take away
# We can use lambda function too
# use of precision and width in fliterals
