# https://www.acmicpc.net/problem/19238
import sys
from collections import deque
import heapq
input = sys.stdin.readline

n, m, oil = map(int, input().split())
end = 0
graph = [[0] * (n + 1)]
for i in range(1, n + 1):
    graph.append(list(map(int, input().split())))
    graph[i].insert(0, 0)
checkNumber = 1
visit = [[0] * (n + 1) for _ in range(n + 1)]


taxiX, taxiY = map(int, input().split())
customer = []
for i in range(m):
    customer.append(list(map(int, input().split())))
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

        for idx in range(len(customer)):
            # 손님을 만나면
            if tx == customer[idx][0] and ty == customer[idx][1]:
                # 현재 거리보다 더 탐색하지 못하게 limit을 검
                limit = min(limit, depth)
                heapq.heappush(heap, (depth, tx, ty, to, customer[idx]))

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
        return heapq.heappop(heap)
    else:
        if end == m:
            print(oil)
        else:
            print(-1)
        exit()
        


def DRIVE(x, y, oil):
    global n, checkNumber, taxiX, taxiY
    que.clear()
    target = START[x][y]
    START[x][y] = 0
    que.append((x, y, oil, 0))
    visit[x][y] = checkNumber

    while que:
        ax, ay, ao, adis = que.popleft()
        if END[ax][ay] == target:
            END[ax][ay] = 0
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
    oil = DRIVE(x, y, o)
    if oil == -1:
        print(oil)
        break
    checkNumber += 1

