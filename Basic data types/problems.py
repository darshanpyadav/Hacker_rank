# Problem 1
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
#
# Input Format
#
# The first line contains . The second line contains an array   of  integers each separated by a space.
#
# Constraints
#
# Output Format
#
# Print the runner-up score.
#
# Sample Input 0
#
# 5
# 2 3 6 6 5

if __name__ == '__main__':
    n = int(input())
    l = map(int, input().split())

    # get unique elements list and sort it
    l = list(set(l))
    l.sort()
    if len(l) == 1:
        print(l[-1])
    else:
        print(l[-2])


# Take away
# sort() doesn't return anything



# Problem 2

# You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and marks for students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
#
# Input Format
#
# The first line contains the integer , the number of students. The next  lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.
#
# Constraints
#
# Output Format
#
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
#
# Sample Input 0
#
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    student_name = input()
    avg = sum(student_marks[student_name])/len(student_marks[student_name])
    print(f'{avg:.2f}')

# Take away
# f literals and usage of *args
