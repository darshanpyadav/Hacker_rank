# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
#
# Input Format
#
# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.
#
# Constraints
#
# There will always be one or more students having the second lowest grade.
# Output Format
#
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
#
# Sample Input 0
#
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0
#
# Berry
# Harry

if __name__ == '__main__':
    n = int(input())

    students = [[input(), float(input())] for _ in range(n)]

    student_marks = [i[1] for i in students]
    student_marks.sort()
    sorted_unique_marks = sorted(list(set(student_marks)))
    second_low_marks = sorted_unique_marks[1]

    # for i in sorted(students):
    #     if i[1] == second_low_marks:
    #         print(i[0])

    print("\n".join([i[0] for i in sorted(students) if i[1] == second_low_marks]))


# Take away
# Use sorted as .sort() returns nothing
# use of list comprehensions
