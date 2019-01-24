from collections import Counter

s, n = input(), int(input())

repeat = n // len(s)
remainder = n % len(s)

total_a = Counter(s)["a"] * repeat + Counter(s[:remainder])["a"]

print(total_a)