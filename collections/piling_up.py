from collections import deque

if __name__ == "__main__":
    # output = []

    # n = int(input())

    # for i in range(n):
    #     _, cubes = input(), map(int, input().split())
    #     cubes = deque(cubes)
    #
    #     while cubes:
    #         if len(cubes) == 2:
    #             output.append("Yes")
    #             break
    #
    #         if max(list(cubes)[1:-1]) > cubes[0] and max(list(cubes)[1:-1]) > cubes[-1]:
    #             output.append("No")
    #             break
    #
    #         if cubes[0] >= cubes[-1]:
    #             cubes.popleft()
    #
    #         else:
    #             cubes.pop()
    #
    # print("\n".join(output))

    # Can't be done cuz of the below reason
    # why are you using a deque if everything you are doing with it can be done with an array? and you are using max in
    # your while loop, so the time complexity is O(n ^ 2) which is too big for some of the input

    # the input needs to be shaped like a mountain with its minimum value at its single peak. We can test the left and
    # right sides of the mountain to see if they "slope", (AKA are sorted) to this peak.

    for t in range(int(input())):
        input()
        lst = list(map(int, input().split()))
        l = len(lst)
        i = 0
        while i < l - 1 and lst[i] >= lst[i + 1]:
            i += 1
        while i < l - 1 and lst[i] <= lst[i + 1]:
            i += 1

        print("Yes" if i == l - 1 else "No")
