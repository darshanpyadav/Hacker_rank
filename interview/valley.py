n, s = input(), input()
valley = 0
pointer = 0

for step in s:
    pointer = pointer + 1 if step == "U" else pointer - 1

    if pointer == 0 and step == "U":
        valley += 1

print(valley)


# Order O(n)