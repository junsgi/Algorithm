# https://www.acmicpc.net/problem/1018
import sys 
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
ans = []

for i in range(n - 7):
    for j in range(m - 7):
        Wdraw = 0
        Bdraw = 0
        # 8 x 8 정사각형 범위 설정
        for x1 in range(i, i + 8):
            for y1 in range(j, j + 8):
                if (x1 + y1) % 2 == 0:
                    if graph[x1][y1] != 'W':
                        Wdraw += 1
                    else:
                        Bdraw += 1
                else:
                    if graph[x1][y1] != 'B':
                        Wdraw += 1
                    else:
                        Bdraw += 1
        ans.append(Bdraw)
        ans.append(Wdraw)
print(min(ans))
