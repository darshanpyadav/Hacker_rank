# ZIP

if __name__ == "__main__":
    _, n = map(int, input().split())

    zip_arr = []
    for i in range(n):
        zip_arr.append(map(float, input().split()))

    print("\n".join([str(sum(i) / len(i)) for i in zip(*zip_arr)]))

# This function returns a list of tuples. The th tuple contains the th element from each of the argument sequences or
# iterables.
#
# If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest
# argument sequence.
# --------------------------------------------------------------------------------------------------------------------
# eval

# eval(var), eval(input())
# >>> x = 2
# >>> eval("x + 3")
# 5

eval(input())

# The eval() expression is a very powerful built-in function of Python. It helps in evaluating an expression.
# The expression can be a Python statement, or a code object.


ui = input().split()
x = int(ui[0])
print(eval(input()) == int(ui[1]))

# Print True if P(x) = k . for x k inputs. Otherwise, print False.
#
# Sample Input
#
# 1 4
# x**3 + x**2 + x + 1
# Sample Output
#
# True

# --------------------------------------------------------------------------------------------------------------------
# any or all

# This expression returns True if any element of the iterable is true.
# If the iterable is empty, it will return Fals
#
# >>> any([1>0,1==0,1<0])
# True
# >>> any([1<0,2<1,3<2])
# False

# This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return
# True.
# >>> all(['a'<'b','b'<'c'])
# True
# >>> all(['a'<'b','c'<'b'])
# False

input()
n = input().split()
print(all([int(i) > 0  for i in n]) and any([int(i) == int(i[::-1]) for i in n]))

# You are given a space separated list of integers. If all the integers are positive, then you need to check if any
# integer is a palindromic integer.

