import  time

if __name__ == "__main__":
    n = input()
    input_list = list(map(int, input().split()))
    a, b = set(map(int, input().split())), set(map(int, input().split()))
    # h = 0
    # s = 0

    start = time.time()
    # for i in input_list:
    #     if i in a:
    #         h += 1
    #     elif i in b:
    #         s += 1
    #     else:
    #         continue
    #
    # print(h - s)
    # Time taken = 0.0000610352

    print(sum([1 if i in a else -1 if i in b else 0 for i in input_list]))
    # print(sum([(i in A) - (i in B) for i in input_list]))   // leveraging True == 1 and False == 0
    # Time taken = 0.0000448227

    print("Time taken = {0:.10f}".format(time.time() - start))

# There is an
# array
# of
# integers.There
# are
# also
# disjoint
# sets, and, each
# containing
# integers.You
# like
# all
# the
# integers in set and dislike
# all
# the
# integers in set.Your
# initial
# happiness is.For
# each
# integer in the
# array,
# if , you add  to your happiness.If, you add  to your happiness.Otherwise, your happiness does not change.Output your final happiness at the end.
#
# Note: Since and are
# sets, they
# have
# no
# repeated
# elements.However, the
# array
# might
# contain
# duplicate
# elements.
#
# Constraints
#
# Input
# Format
#
# The
# first
# line
# contains
# integers and separated
# by
# a
# space.
# The
# second
# line
# contains
# integers, the
# elements
# of
# the
# array.
# The
# third and fourth
# lines
# contain
# integers, and, respectively.
#
# Output
# Format
#
# Output
# a
# single
# integer, your
# total
# happiness.
#
# Sample
# Input
#
# 3
# 2
# 1
# 5
# 3
# 3
# 1
# 5
# 7
# Sample
# Output
#
# 1
# Explanation
#
# You
# gain
# unit
# of
# happiness
# for elements and in set.You lose  unit for in set.The element in set  does not exist in the array so it is not included in the calculation.
#
# Hence, the
# total
# happiness is.