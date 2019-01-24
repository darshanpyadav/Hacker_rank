def wrapper(f):
    def fun(l):
        f("+91 " + str(i[-10:-5]) + " " + str(i[-5:]) for i in l)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)



# Key taekaways
# Usage of generators and list comprehension an *