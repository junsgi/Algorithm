# https://www.acmicpc.net/problem/1799
import sys
input = sys.stdin.readline
def BACK(depth, cnt):
    global ans, n
    
    if depth == len(location):
        ans = max(ans, cnt)
        return
    
    if ans == n + (n - 2):
        if not depth : ans += 1
        print(ans)
        exit()
    # 현재 사용중인 비숍 + (더 놓을 수 있는 비숍 개수)
    if cnt + (len(location) - depth) <= ans: return
    x, y = location[depth][0], location[depth][1]
    if not (left[x - y + n] + right[x + y]): # 선택한다
        left[x - y + n] = right[x + y] = 1
        BACK(depth + 1, cnt + 1)
        left[x - y + n] = right[x + y] = 0

    # 안 한다.
    BACK(depth + 1, cnt)
n = int(input())
ans = 0
left = [0] * (50)
right = [0] * (50)
location = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j]:
            location.append([i, j])

BACK(0, 0)
print(ans)
"""
최악의 경우 2 ^ 100번 만큼 연산을 하게됨
2 * 2의 경우 최대로 놓을 수 있는 개수 = 2
3 * 3의 경우 최대로 놓을 수 있는 개수 = 4
4 * 4의 경우 최대로 놓을 수 있는 개수 = 6
즉 비숍이 n + (n - 2)개 놓이면 최대로 놓았으므로 더이상 탐색하지 않는다.

3
1 1 1
1 1 1
1 1 1

ans:4

--------------------------------------------

4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1

ans:6

--------------------------------------------

5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1

ans:8

--------------------------------------------

8
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1

ans:14

--------------------------------------------

10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1

ans:18

여기까지 되면 시간복잡도는 충분하다.

--------------------------------------------

5
1 1 0 1 1
0 1 0 0 1
1 0 1 0 1
1 0 0 0 0
1 0 1 1 1

ans:8

--------------------------------------------

5
0 0 0 0 0
0 1 0 1 0
1 0 0 0 1
0 1 0 1 0
0 0 0 0 0

ans:3

--------------------------------------------

5
0 0 0 1 0
0 0 1 0 0
0 1 0 1 0
0 0 1 0 0
0 0 0 1 0

ans:3
"""