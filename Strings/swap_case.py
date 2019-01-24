# def swap_case(sequence):
#     s = ""
#     for letter in sequence:
#         if letter.isupper():
#             s += letter.lower()
#         elif letter.islower():
#             s += letter.upper()
#         else:
#             s += letter
#     return s
#
#
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


if __name__ == '__main__':
    s = input()
    print("".join([i.lower() if i.isupper() else i.upper() for i in s]))


# Take away
# list comprehension if and else