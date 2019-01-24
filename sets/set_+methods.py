n = int(input())
s = set(map(int, input().split()))

command_num = int(input())
command_set = [input() for command in range(command_num)]

for command in command_set:
    if command == "pop":
        s.pop()
    else:
        eval("s." + command.split()[0] + "(" + command.split()[1] + ")")

print(sum(s))
# -------------------------------------------------------------------------------------------------------------

e = int(input())
e_set = set(map(int, input().split()))
f = int(input())
f_set = set(map(int, input().split()))
print(len(e_set | f_set))

# -------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = int(input())
    answers = []

    for i in range(test_cases):
        _, m_set, _, n_set = input(), set(map(int, input().split())), input(), set(map(int, input().split()))
        answers.append(str(m_set.issubset(n_set)))

    print("\n".join(answers))
# -------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    # input_set = set(map(int, input().split()))
    # test_cases = int(input())
    #
    # for _ in range(test_cases):
    #     set_i = set(map(int, input().split()))
    #     if input_set.issuperset(set_i) and len(input_set) == len(set_i):
    #         print("False")
    #         break
    #     else:
    #         print("False")
    #         break
    # else:
    #     print("True")
    a = set(input().split())
    print(all([a > set(input().split()) for _ in range(int(input()))]))

# -------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    _, input_set = input(), set(map(int, input().split()))

    for _ in range(int(input())):
        eval("input_set." + input().split()[0] + "(" + str(set(map(int, input().split()))) + ")")

    print(sum(input_set))

# -------------------------------------------------------------------------------------------------------------

# Take away
# Usage of all -> function
# Error: object is not subscriptable : means there is an non-indexable object
# -------------------------------------------------------------------------------------------------------------

# s = set()
# s.add()
# s.update()
# s.remove(key) == s.discard(key)  discard doesn't raise the key error
# s.pop() removes arbitrary element
# s.union(s1) or s | s1
# s.intersection(s1) or s & s2
# s.difference(s1) or s - s1 //elem only in s
# s.symmetric_difference(s1) or s ^ s1  // union - intersection

# update the original set itself
# s.update(), s.intersection_update(s1), s.difference_update(s1), s.symmetric_difference_update(s1)
# super set  s > s1
# Disjoint set: When there are no elements in common: {'a'}.isdisjoint({'a','b'})
