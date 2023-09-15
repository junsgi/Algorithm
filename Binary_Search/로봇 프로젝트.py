# https://www.acmicpc.net/problem/3649
import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input().strip()) * 10000000
    except:
        break
    n = int(input().strip())
    swi = False
    if n == 0: 
        print('danger')
        continue
    a = []
    for _ in range(n):
        a.append(int(input()))
    a.sort()
    p1 = 0
    p2 = n - 1
    while p1 != p2:
        s = a[p1] + a[p2]
        if x == s:
            print(f'yes {a[p1]} {a[p2]}')
            swi = True
            break
        elif x < s:
            p2 -= 1
        else:
            p1 += 1
    if not swi:
        print('danger')