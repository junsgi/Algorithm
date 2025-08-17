import sys
from collections import deque

dire = [[-1, 1, 0 ,0], [0, 0, -1, 1]]

# 너비 우선 탐색
def BFS(n, m, key):
    global cheeseCnt
    que = deque()
    que.append([0, 0])

    while len(que) != 0:
      temp = que.popleft()

      x1 = temp[0]
      y1 = temp[1]

      for i in range(4):

        if x1 + dire[0][i] < 0 or x1 + dire[0][i] >= n: continue
        if y1 + dire[1][i] < 0 or y1 + dire[1][i] >= m: continue
        if freq[x1 + dire[0][i]][y1 + dire[1][i]] == key: continue

        freq[x1 + dire[0][i]][y1 + dire[1][i]] = key

        if arr[x1 + dire[0][i]][y1 + dire[1][i]] == 1:
            cheeseCnt += 1
            arr[x1 + dire[0][i]][y1 + dire[1][i]] = 0

        elif arr[x1 + dire[0][i]][y1 + dire[1][i]] == 0:
            que.append([x1 + dire[0][i], y1 + dire[1][i]])
    return


n, m =  map(int,sys.stdin.readline().split())
arr = []
freq = [[0 for i in range(m)] for j in range(n)]

# 1의 개수를 세어 없어질 때까지 반복합니다.
cheese = 0

# 없어지기전 마지막 치즈
ans = 0

# 횟수
cnt = 0

# 함수에서도 쓰일 전역변수 
# 탐색 한 번에 얼만큼 치즈가 녹았는지 기록
cheeseCnt = 0


for _ in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    cheese += temp.count(1)
    arr.append(temp)

# 빈도 배열에서 key 변수를 이용하여 탐색할 부분과 탐색하지 않을 부분을 구분합니다.
key = 2

# 치즈가 다 녹아 없어질 때 동안
while cheese != 0:

    cheeseCnt = 0
    freq[0][0] = key
    BFS(n, m, key)
    ans = cheese
    cheese -= cheeseCnt
    cnt += 1
    key += 1

ans = str(cnt) + '\n' + str(ans)
print(ans)