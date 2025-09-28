"""
Count the Notebooks

You know that 
1 kg of pulp can be used to make 1000 pages 
and 1 notebook consists of 100 pages.

Suppose a notebook factory receives N kg of pulp, 
how many notebooks can be made from that?

Input Format:
    • First line will contain T, the number of test cases. 
    • Each test case contains a single integer N - 
      the weight of the pulp the factory has (in kgs).

Output Format:
    For each test case, output the number of notebooks 
    that can be made using N kgs of pulp.
"""

T = int(input())
for _ in range(T):
    N = int(input())
    print(N * 10)