'''
Chefland Games 
-----------------------------------
In Chefland, a tennis game involves 4 referees.
Each referee decides whether the ball is inside (0) or outside (1).
The ball is considered "IN" if and only if ALL referees say 0.
Otherwise, it is "OUT".

Input:
  - First line: integer T (number of test cases)
  - Next T lines: 4 integers (R1, R2, R3, R4) each being 0 or 1

Output:
  - "IN" if all referees say 0
  - "OUT" otherwise
'''

T = int(input().strip())

for _ in range(T):
    R1, R2, R3, R4 = map(int, input().split())
    if R1 == R2 == R3 == R4 == 0:
        print("IN")
    else:
        print("OUT")
