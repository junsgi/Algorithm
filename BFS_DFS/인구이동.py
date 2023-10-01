import sys
from collections import deque
input = sys.stdin.readline

def BFS(x, y, check):
    global n, L, R
    que.clear()
    que.append((x, y))
    freq[x][y] = check
    sum = a[x][y]
    num = 1
    while que:
        ax, ay = que.popleft()

        for i, j in dire:
            tx, ty = ax + i, ay + j
            
            if not (0 <= tx < n and 0 <= ty < n): continue
            if freq[tx][ty] == check: continue
            if not (L <= abs(a[ax][ay] - a[tx][ty]) <= R): continue
            sum += a[tx][ty]
            num += 1
            freq[tx][ty] = check
            que.append((tx, ty))

    return sum // num

# 체크했던 곳을 탐색하며 인구수를 수정한다.
def MOVE(Tque):
    global n
    while Tque:
        ax, ay, result, check = Tque.popleft()
        freq[ax][ay] = 0
        a[ax][ay] = result
        for i, j in dire:
            tx, ty = ax + i, ay + j
            if not (0 <= tx < n and 0 <= ty < n): continue
            if freq[tx][ty] != check: continue
            freq[tx][ty] = 0
            a[tx][ty] = result
            Tque.append((tx, ty, result, check))


# 상하좌우에 국경선을 열 수 있는 나라가 있는지 확인
def CHECK(x, y):
    for i, j in dire:
        tx, ty = x + i, y + j
        if not (0 <= tx < n and 0 <= ty < n): continue
        if L <= abs(a[x][y] - a[tx][ty]) <= R:
            return True
    return False

n, L, R = map(int, input().strip().split())
a = [list(map(int, input().strip().split())) for i in range(n)]
que = deque()
freq = [[0] * n for i in range(n)]
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cnt = 0
answer = 0
temp = deque()
while True:
    for i in range(n):
        for j in range(n):
            if not freq[i][j] and CHECK(i, j):
                cnt += 1
                temp.append((i, j, BFS(i, j, cnt), cnt))

    if temp:
        answer += 1
    else: break

    MOVE(temp)
    temp.clear()
        
print(answer)