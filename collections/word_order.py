from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


if __name__ == "__main__":
    n = int(input())

    counter = OrderedCounter([input().strip() for i in range(n)]).values()

    print(len(counter))
    print(*counter)


# Key takeaways
# Creation of new orderedCounter class
# When we use dict method on Counter, the order messes up
# so using class uses Ordereddict
