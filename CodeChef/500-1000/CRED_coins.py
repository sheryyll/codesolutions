# CRED Coins Problem
# For each bill you pay using CRED, you earn X CRED coins.
# At CodeChef store, each bag is worth 100 CRED coins.
# Chef pays Y number of bills using CRED. 
# Find the maximum number of bags he can get from the CodeChef store.

# Input Format:
# First line will contain T, number of test cases.
# Each test case contains a single line of input, two integers X and Y.
#
# Output Format:
# For each test case, output in a single line - 
# the maximum number of bags Chef can get from the CodeChef store.

# ------------------ Solution ------------------


T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())

    total_coins = X * Y
    bags = total_coins // 100
    print(bags)
