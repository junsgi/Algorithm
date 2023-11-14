# https://www.acmicpc.net/problem/2632
P = int(input())
n, m = map(int, input().split())
t = []
for _ in range(n + m): t.append(int(input()))
A = t[:n]
B = sorted(t[n:])
tA = []