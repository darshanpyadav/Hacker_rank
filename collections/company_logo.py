from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


if __name__ == "__main__":
    seq = input()

    out = OrderedCounter(sorted(seq)).most_common(3)

    for i in out:
        print(*i)


# TAKE AWAY
# use of Counter and ordered dict at once
