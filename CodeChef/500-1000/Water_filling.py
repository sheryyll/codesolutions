"""
Problem: Water Bottles (Chef Water Filling Time)

Chef has three water bottles. At any point, if at least two of them are empty,
she will fill them up. But if at most one bottle is empty, she will wait,
and not fill them up now.

You are given three integers - B1, B2, and B3.
If B1 = 1, it means that the first bottle is full.
If B1 = 0, it means that the first bottle is empty.
Similarly, B2 denotes whether the second bottle is full or empty,
and B3 denotes it for the third bottle.

Output "Water filling time" if Chef has to fill the bottles now.
If not, output "Not now".

-------------------------
Input Format:
The first line contains a single integer T, the number of test cases.
Each test case contains three space-separated integers B1, B2, B3.

Output Format:
For each test case, output on a new line:
- "Water filling time" if Chef fills bottles.
- "Not now" otherwise.
"""

t = int(input().strip())
  for _ in range(t):
      b1, b2, b3 = map(int, input().split())
      empty_count = (b1 == 0) + (b2 == 0) + (b3 == 0)

      if empty_count >= 2:
        print("Water filling time")
      else:
        print("Not now")


