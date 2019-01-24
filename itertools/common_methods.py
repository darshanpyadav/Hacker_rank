from itertools import *

if __name__ == "__main__":
    A, B = list(map(int, input().split())), list(map(int, input().split()))

    print(" ".join([str(i) for i in product(A, B)]))


# product() -> returns the cartesian product of iterables
#
# >>> from itertools import product
# >>>
# >>> print list(product([1,2,3],repeat = 2))
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
# >>>
# >>> print list(product([1,2,3],[3,4]))
# [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
# >>>
# >>> A = [[1,2,3],[3,4,5]]
# >>> print list(product(*A))
# [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
# >>>
# >>> B = [[1,2,3],[3,4,5],[7,8]]
# >>> print list(product(*B))
# [(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7),
#  (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    string, r = input().split()

    print("\n".join(["".join(i) for i in permutations(sorted(string), int(r))]))


# Permutations is arranging n set of objects in r different ways.
# npr = n!//(n-r)!
# >>> from itertools import permutations
# >>> print permutations(['1','2','3'])
# <itertools.permutations object at 0x02A45210>
# >>>
# >>> print list(permutations(['1','2','3']))
# [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
# >>>
# >>> print list(permutations(['1','2','3'],2))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
# >>>
# >>> print list(permutations('abc',3))
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    string, r = input().split()

    for k in range(1, int(r) + 1):
        print("\n".join(["".join(i) for i in combinations(sorted(string), k)]))

# Combinations is selection of n different elements r at a times
# # nCr = n!//(n-r)!*r!
# >>> from itertools import combinations
# >>>
# >>> print list(combinations('12345',2))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'),
# ('4', '5')]
# >>>
# >>> A = [1,1,3,3,3]
# >>> print list(combinations(A,4))
# [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    string, r = input().split()

    print("\n".join(["".join(i) for i in combinations_with_replacement(sorted(string), int(r))]))

# length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
# (n+r-1)! // r! * (n-1)!
# print list(combinations_with_replacement('12345',2))
# [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'),
# ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
# >>>
# >>> A = [1,1,3,3,3]
# >>> print list(combinations(A,2))
# [(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]
