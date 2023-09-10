import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline
def MOVE(x, y, d): pass
back = [2, 3, 0, 1] 
dire = [[-1, 0], [0, 1], [1, 0], [0, -1]]
change = [3, 0, 1, 2]
n, m = map(int, input().strip().split())
rx, ry, d = map(int, input().strip().split())
a = [list(map(int, input().strip().split())) for _ in range(n)]
ans = 0
MOVE(rx, ry, d)
print(ans)
for i in a:
    print(i)