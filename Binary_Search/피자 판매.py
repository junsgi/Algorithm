# https://www.acmicpc.net/problem/2632
P = int(input())
n, m = map(int, input().split())
AB = sorted([int(input()) for _ in range(n + m)])
print(AB)
p1 = 0
p2 = (n + m) - 1
ans = 0
while p1 != p2:

    mid = AB[p1] + AB[p2]
    if mid == P: ans += 1
    
    if mid >= P:
        p2 -= 1
    else:
        p1 += 1
print(ans)