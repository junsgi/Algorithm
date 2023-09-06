# https://www.acmicpc.net/problem/9205
import sys
from collections import deque
input = sys.stdin.readline
n = int(input().strip())
que = deque()
for i in range(n):
    t = int(input().strip())
    que.clear()
    dab = "sad"
    house = list(map(int, input().strip().split()))
    store = []
    for j in range(t):
        store.append(list(map(int, input().strip().split())))
    freq = [0] * len(store)

    end = list(map(int, input().strip().split()))
    que.append(house)
    while que:
        x, y = que.popleft()
        # 현재 위치에서 맥주 20병 마실동안 도착할 수 있다면 break
        if abs(x - end[0]) + abs(y - end[1]) <= 1000: 
            dab = "happy"
            break

        # 참조했거나 거리가 안되면 que에 넣지 않습니다.
        for j in range(len(store)): 
            sx, sy = store[j][0], store[j][1]
            if freq[j]: continue
            if abs(x - sx) + abs(y - sy) > 1000:continue
            freq[j] = 1
            que.append((sx, sy))
    print(dab)