import time


def count_substring(string, sub_string):
    # part 1. Time taken is 0.00007
    # for
    # ABCDCDC
    # CDC

    # count_sub = 0
    # for i in range(len(string) - len(sub_string) + 1):
    #     if string[i:i + len(sub_string)] == sub_string:
    #         count_sub += 1
    # return count_sub

    # part2. Time taken is 0.00006
    return sum([1 for i in range(len(string) - len(sub_string) + 1) if string[i: i + len(sub_string)] == sub_string])


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    start = time.time()
    count = count_substring(string, sub_string)
    print(count)
    print("Time taken = {0:.5f}".format(time.time() - start))


# Take away
# slicing and usage of sum