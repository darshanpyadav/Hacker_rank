t = int(input())
result = []

for i in range(t):
    n = int(input())
    ar = list(map(int, input().split()))

    j = 0
    bribe_val = 0
    while j < len(ar):
        # print(j)
        val = abs(ar[j] - ar[j+1])
        if val > 2:
            result.append("Too chaotic")
            break
        j += val + 1
        bribe_val += val
    else:
        result.append(str(bribe_val))

print("\n".join(result))
