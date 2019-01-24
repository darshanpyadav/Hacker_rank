if __name__ == '__main__':
    i = input()
    n, m = map(int, i.split())

    # pattern = ".|."
    #
    # for i in range(n//2):
    #     print(((1 + 2 * i) * pattern).center(m, "-"))
    #
    # print("WELCOME".center(m, "-"))
    #
    # for i in range(1, n//2 + 1):
    #     print(((n - 2 * i) * pattern).center(m, "-"))

    pattern = [(".|."*(1 + 2*i)).center(m, "-") for i in range(n//2)]

    print("\n".join(pattern + ["WELCOME".center(m, "-")] + pattern[::-1]))


# take away
# usage of reversal of pattern printing using list reversal list[::-1]
