# Problem: Exams
# In Chefland, there are X schools, and each school has Y students.
# The year end results are in and a total of Z students passed the exams.
#
# Assuming that all students appeared for the exams, find whether the number of
# students who passed in Chefland was strictly greater than 50%.
#
# Input Format:
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of three space-separated integers X, Y, and Z.
#
# Output Format:
# For each test case, output on a new line:
#   - "YES" if the total number of students who passed in Chefland was strictly greater than 50%
#   - "NO" otherwise.
#
# You may print each character of the string in uppercase or lowercase
# (for example, YES, yEs, yes, and yeS will all be treated as identical).

T = int(input())

for _ in range(T):
    X, Y, Z = map(int, input().split())
    total_students = X * Y
    
    if Z > total_students / 2:
        print("YES")
    else:
        print("NO")
