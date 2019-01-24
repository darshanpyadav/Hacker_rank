from cmath import *

pow(2, 3)
pow(2, 3, 5)
divmod(177, 10)
# -------------------------------------------------------------------------------------------------------------
inp = input()

print(abs(complex(inp)))
print(phase(complex(inp)))

# -------------------------------------------------------------------------------------------------------------
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10 ** i // 9) * i)

# prints below for n = 5
# 1
# 22
# 333
# 4444
# -------------------------------------------------------------------------------------------------------------

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10 ** i - 1) ** 2 // 81)

# prints below for n = 5
# 1
# 121
# 12321
# 1234321
# 123454321
# These are called Demlo numbers
# -------------------------------------------------------------------------------------------------------------
import math

AB, BC = int(input()), int(input())

print(str(int(round(math.degrees(math.atan2(AB, BC)))))+'°')


# Find the angle made by the median at the right angled triangle

# -------------------------------------------------------------------------------------------------------------
# basics
# power can be calculated by pow function or a ** b
# pow function accepts 3rd argument mod.
# mod gives the remainder of integer division
# divmod returns the quotient and remainder divmod(177,10) == (17,7)
# // is integer division