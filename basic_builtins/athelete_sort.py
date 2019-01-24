def sort_key(elem):
    return elem[k]


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=sort_key)

    for i in arr:
        print(*i)


# Take away
# Sort accepts a function argument which you can define to base the sorting on
