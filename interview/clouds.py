_, ar = input(), input().split()
i, jump = 0, 0

while i <= len(ar) - 2:
    if i + 2 < len(ar) and ar[i + 2] != "1":
        i += 1
    jump += 1
    i += 1

print(jump)
