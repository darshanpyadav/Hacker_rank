import re

for _ in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)

# Errors during execution are called exceptions

for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:", e)

while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            print(val)
            break
        finally:
            print("Finally, I executed!")

        print(val)

# Please enter an integer: a
# Looks like you did not enter an integer!
# Finally, I executed!
# Please enter an integer: 12
# Yep that's an integer!
# 12
# Finally, I executed!
