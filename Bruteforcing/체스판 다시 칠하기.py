# https://www.acmicpc.net/problem/1018
import sys 
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(lambda x : 1 if x == 'W' else -1, input())) for _ in range(n)]
s = 0
ans = 0
for i in graph:
    s = sum(i)
    ans += abs(s) - 1
print(ans - 1)