import math

# fibonocci

memo = {0:0, 1:1}


def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]

print(fibm(7))

# Think of a recusive version of the function f(n) = 3 * n, i.e. the multiples of 3


def f(n):
    if n == 1:
        return 3
    else:
        return 3 + f(n-1)


print(f(3))

# Write a recursive Python function that returns the sum of the first n integers.


def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n-1)


print(sum_n(2))

# Write a function which implements the Pascal's triangle:

#                     1
#                 1    1
#             1    2    1
#         1    3    3    1
#    1   4    6    4    1
# 1    5    10    10    5    1


def pascal(n):
    if n == 1:
        print(1)
        return [1]
    else:
        prev_l = pascal(n-1)
        current = [prev_l[i] + prev_l[i+1] for i in range(len(prev_l) - 1)]
        current.insert(0, 1)
        current.append(1)
        print(*current)
        return current


pascal(7)

# The Fibonacci numbers are hidden inside of Pascal's triangle. If you sum up the coloured numbers of the following
# triangle, you will get the 7th Fibonacci number:


def fib_pascal(n, fib_pos):
    if n == 1:
        line = [1]
        fib_sum = 1 if fib_pos == 0 else 0
    else:
        previous_line, fib_sum = fib_pascal(n-1, fib_pos+1)
        line = [previous_line[i] + previous_line[i+1] for i in range(len(previous_line)-1)]
        line.insert(0, 1)
        line.append(1)
        if fib_pos < len(line):
            fib_sum += line[fib_pos]

    return line, fib_sum


def fib(n):
    return fib_pascal(n, 0)[1]


print(fib(7))

'''
Implement a recursive function in Python for the sieve of Eratosthenes.
The sieve of Eratosthenes is a simple algorithm for finding all prime numbers up to a specified integer. It was created 
by the ancient Greek mathematician Eratosthenes. 
The algorithm to find all the prime numbers less than or equal to a given integer n:

Create a list of integers from two to n: 2, 3, 4, ..., n
Start with a counter i set to 2, i.e. the first prime number
Starting from i+i, count up by i and remove those numbers from the list, i.e. 2*i, 3*i, 4*i, aso..
Find the first number of the list following i. This is the next prime number.
Set i to the number found in the previous step
Repeat steps 3 and 4 until i is greater than n. (As an improvement: It's enough to go to the square root of n)
All the numbers, which are still in the list, are prime numbers

You can easily see that we would be inefficient, if we strictly used this algorithm, e.g. we will try to remove the 
multiples of 4, although they have been already removed by the multiples of 2. So it's enough to produce the multiples
of all the prime numbers up to the square root of n. We can recursively create these sets. 
'''


from math import sqrt


def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = [j for i in p for j in range(i*2, n + 1, i)]
        p = [x for x in range(2, n + 1) if x not in no_p]
        return p


print(primes(100))


# Write a recursive function find_index(), which returns the index of a number in the Fibonacci sequence, if the number
# is an element of this sequence and returns -1 if the number is not contained in it, i.e.
# fib(find_index(n)) == n


memo = {0:0, 1:1}


def fib(n):
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

ß
def find_index(*x):
    """ finds the natural number i with fib(i) = n """
    if len(x) == 1:
        # started by user
        # find index starting from 0
        return find_index(x[0], 0)
    else:
        n = fib(x[1])
        m = x[0]
        if n > m:
            return -1
        elif n == m:
            return x[1]
        else:
            return find_index(m, x[1]+1)
