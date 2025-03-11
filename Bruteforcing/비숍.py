# https://www.acmicpc.net/problem/1799
import sys 
input = sys.stdin.readline
def BACK(depth, cnt, sel):
    global n
    
    if depth == len(location[sel]):
        ans[sel] = max(ans[sel], cnt)
        return
    # 현재 사용중인 비숍 + (더 놓을 수 있는 비숍 개수)
    if cnt + (len(location[sel]) - depth) <= ans[sel]: return
    
    
    x, y = location[sel][depth][0], location[sel][depth][1]
    if not (left[x - y + n] + right[x + y]): # 선택한다
        left[x - y + n] = right[x + y] = 1
        BACK(depth + 1, cnt + 1, sel)
        left[x - y + n] = right[x + y] = 0

    # 안 한다.
    BACK(depth + 1, cnt, sel)
n = int(input())
ans = [0, 0]
left = [0] * (50)
right = [0] * (50)
location = [[], []]
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j]:
            location[(i + j) % 2].append([i, j])
BACK(0, 0, 0)
BACK(0, 0, 1)
print(ans)
print(ans[0] + ans[1])
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