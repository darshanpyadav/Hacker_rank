from collections import OrderedDict


def merge_the_tools(input_str, step):
    l = [input_str[i: i + step] for i in range(0, len(input_str), step)]

    # removing duplicates using ordereddict
    print("\n".join(["".join(OrderedDict.fromkeys(sub_str)) for sub_str in l]))

    # your code goes here
    l = []
    # out_list = []
    # m = 0
    # n = step
    # for i in range(len(input_str) // step):
    #     l.append(input_str[m:n])
    #     m = n
    #     n = (i + 2) * step

    # for j in l:
    #     out_str = ""
    #     for k in j:
    #         if k in out_str:
    #             pass
    #         else:
    #             out_str += k
    #     out_list.append(out_str)
    # print("\n".join([i for i in out_list]))


if __name__ == '__main__':
    string, size = input(), int(input())
    merge_the_tools(string, size)


# Take away
# Usage of range paramters i.e step to split based on step size
# usage of ordereddict to remove duplicate elements in order

# Consider the following:
#
# A string, , of length  where .
# An integer, , where  is a factor of .
# We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:
#
# The characters in  are a subsequence of the characters in .
# Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
# Given  and , print  lines where each line  denotes string .
#
# Input Format
#
# The first line contains a single string denoting .
# The second line contains an integer, , denoting the length of each subsegment.
#
# Constraints
#
# , where  is the length of
# It is guaranteed that  is a multiple of .
# Output Format
#
# Print  lines where each line  contains string .
#
# Sample Input
#
# AABCAAADA
# 3
# Sample Output
#
# AB
# CA
# AD