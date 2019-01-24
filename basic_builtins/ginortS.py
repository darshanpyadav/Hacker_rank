if __name__ == "__main__":

    lower = []
    upper = []
    odd = []
    even = []

    for i in input():
        if i.isalpha():
            if i.islower():
                lower.append(i)
            else:
                upper.append(i)
        else:
            if int(i) % 2 != 0:
                odd.append(int(i))
            else:
                even.append(int(i))

    print("".join(sorted(lower) + sorted(upper) + list(map(str, sorted(odd))) + list(map(str, sorted(even)))))

# key takeways
# usage of sort and list