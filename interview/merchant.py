from collections import defaultdict, Counter

_, ar = input(), input().split()
pairs = 0

# d = defaultdict(lambda: 0)
# for i in ar:
#     d[i] += 1
#
# for v in d.values():
#     pairs += v // 2
#
# print(pairs)
#
# # Order = O(n)

c = Counter(ar)

for v in c.values():
    pairs += v // 2

print(pairs)