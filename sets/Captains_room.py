# if __name__ == "__main__":
#     n, list_input = input(), input().split()
#     set_input = set(list_input)
#
#     for i in set_input:
#         if list_input.count(i) == 1:
#             print(i)
#             break
# Time out error for using for loop


# sum(list_input)= k(r1+r2.....rn)+c        ....eqn(1)
# sum(set_input)= (r1+r2+.......rn)+c       ....eqn(2)
# k*eqn(2)-eqn(1) = k*c-c
# c = (k*eqn(2)-eqn(1))/k-1

if __name__ == "__main__":
    k, list_input = int(input()), list(map(int, input().split()))
    set_input = set(list_input)
    print((k * sum(set_input) - sum(list_input))//(k-1))

# take away
# use of maths and avoiding for loops

# ------------------------------------------------------------------------------------------------------

# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
#
# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of  members per group where  ≠ .
#
# The Captain was given a separate room, and the rest were given one room per group.
#
# Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear  times per group except for the Captain's room.
#
# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of  and the room number list.
#
# Input Format
#
# The first line consists of an integer, , the size of each group.
# The second line contains the unordered elements of the room number list.
#
#
# Constraints
#
#
# Output Format
#
# Output the Captain's room number.
#
# Sample Input
#
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
# Sample Output
#
# 8
