# Input Format
#
# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.
#
# Constraints
#
# The elements added to the list must be integers.
# Output Format
#
# For each command of type print, print the list on a new line.
#
# Sample Input 0
#
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0
#
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

if __name__ == '__main__':
    result = []  # initializing result list

    N = int(input())

    for i in range(N):
        command = input()
        command = command.split()
        if command[0] != "print":
            eval("result." + command[0] + "(" + ",".join(command[1:]) + ")")
        else:
            print(result)


# Take away
#
# eval(str) -> evaluates string represenatation of python expression