def fibonacci(n):
    a = [0, 1]
    for i in range(2, n):
        a.append(a[i-2] + a[i-1])
    return a[:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(lambda x: x ** 3, fibonacci(n))))


# use of map
