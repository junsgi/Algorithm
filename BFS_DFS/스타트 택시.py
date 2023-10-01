# https://www.acmicpc.net/problem/19238
import sys
from collections import deque
import heapq
input = sys.stdin.readline

n, m, oil = map(int, input().split())
graph = [[0] * (n + 1)]
for i in range(1, n + 1):
    graph.append(list(map(int, input().split())))
    graph[i].insert(0, 0)
visit = [[0] * (n + 1) for _ in range(n + 1)]

taxiX, taxiY = map(int, input().split())
START = [[0] * (n + 1) for _ in range(n)]

ctm = {}
for i in range(m):
    customer = list(map(int, input().split()))
    START[customer[0]][customer[1]] = i + 2
    ctm[f'{customer[0]} {customer[1]}'] = (customer[2], customer[3])

checkNumber = 1 # 탐색할 때마다 방문배열을 초기화하지 않고 특정 숫자를 참고하여 중복 방문을 막음
end = 0 # 손님을 목적지에 도착할 때마다 1씩 증가
heap = [] 
que = deque()
dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def searchBFS(x, y, oil):
    global n, checkNumber, end
    que.clear()
    heap.clear()
    que.append((x, y, oil, 0))
    visit[x][y] = checkNumber
    limit = 0x7fffffff

    while que:
        tx, ty, to, depth  = que.popleft()
        key = f'{tx} {ty}'
        if key in ctm: # 손님을 만났다면
            limit = min(limit, depth) # 깊이 제한
            heapq.heappush(heap, (depth, tx, ty, to, ctm[key], key))

        for a, b in dire:
            ax, ay = tx + a, ty + b
            if not (1 <= ax <= n and 1 <= ay <= n): continue
            
            # 벽이거나 참조했으면 continue
            if graph[ax][ay] == 1 or visit[ax][ay] == checkNumber: continue

            # 다음 장소 이동 못하면 continue
            if to - 1 <= 0 : continue

            # 제한된 깊이보다 더 탐색하려고 한다면 continue
            if depth + 1 > limit : continue

            que.append((ax, ay, to - 1, depth + 1))
            visit[ax][ay] = checkNumber
    if heap:
        end += 1
        checkNumber += 1
        value = heapq.heappop(heap)
        ctm.pop(value[-1])
        return value
    else: # 손님을 만난적 없지만 모두 데려다 줬으면 답 출력 후 종료
        if end == m:
            print(oil)
        else:
            print(-1)
        exit()
        


def DRIVE(x, y, oil, targetX, targetY):
    global n, checkNumber, taxiX, taxiY
    que.clear()
    START[x][y] = 0
    que.append((x, y, oil, 0))
    visit[x][y] = checkNumber

    while que:
        ax, ay, ao, adis = que.popleft()

        # 목표에 도착
        if ax == targetX and ay == targetY:
            # 택시 위치 수정
            taxiX, taxiY = ax, ay
            # 현재 오일에 주행거리의 2배가 충전된다.
            return adis * 2 + ao
        
        for a, b in dire:
            tx, ty = ax + a, ay + b
            if not ( 1 <= tx <= n and 1 <= ty <= n): continue
            if visit[tx][ty] == checkNumber : continue
            if graph[tx][ty] == 1 : continue
            if ao - 1 < 0 : continue
            que.append((tx, ty, ao - 1, adis + 1))
            visit[tx][ty] = checkNumber
    return -1

while True:
    value = searchBFS(taxiX, taxiY, oil)
    oil = DRIVE(*(value[1:4]), *(value[-2]))
    if oil == -1: # 주행 중 기름이 떨어져 더이상 이동할 수 없다면
        print(oil)
        break
    checkNumber += 1