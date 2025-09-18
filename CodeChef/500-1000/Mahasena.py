"""
Mahasena

Kattapa, as you all know was one of the greatest warriors of his time. 
The kingdom of Maahishmati had never lost a battle under him (as army-chief), 
and the reason for that was their really powerful army, also called as Mahasena.

Kattapa was known to be a very superstitious person. 
He believed that a soldier is "lucky" if the soldier is holding an even number of weapons, 
and "unlucky" otherwise. 
He considered the army as "READY FOR BATTLE" if the count of "lucky" soldiers 
is strictly greater than the count of "unlucky" soldiers, 
and "NOT READY" otherwise.

Input Format:
The first line of input consists of a single integer N denoting the number of soldiers. 
The second line of input consists of N space separated integers A1, A2, ..., AN, 
where Ai denotes the number of weapons that the ith soldier is holding.

Output Format:
Generate one line output saying "READY FOR BATTLE", 
if the army satisfies the conditions that Kattapa requires 
or "NOT READY" otherwise.
"""

# ------------------- Solution -------------------

N = int(input())                
A = list(map(int, input().split()))   

lucky = 0
unlucky = 0

for weapons in A:
    if weapons % 2 == 0:   # even -> lucky
        lucky += 1
    else:                  # odd -> unlucky
        unlucky += 1

if lucky > unlucky:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
