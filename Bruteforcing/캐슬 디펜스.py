# https://www.acmicpc.net/problem/17135
import sys
import copy
import heapq
input = sys.stdin.readline
n, m, d = map(int, input().split())
archer = [[-1, -1] for _ in range(3)]
a = []
enemy = []
heap = []
ans = 0
for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(m):
        if a[i][j] == 1:
            enemy.append((i, j))

def START():
    global n, m, d
    a_copy = copy.deepcopy(a)
    temp = []
    cnt = 0
    # 적 아래로 이동 (성이 한 칸 위로 올라감)
    for ax in range(n, 0, -1):
        temp.clear()
        archer[0][0] = archer[1][0] = archer[2][0] = ax

        # i번째 궁수가 가장 가까우면서 왼쪽에 있는 적 고름
        for i in range(3):
            heap.clear()

            # 적 위치 확인 후 
            for ei, ej in enemy:
                distance = abs(ei - archer[i][0]) + abs(ej - archer[i][1])

                # 궁수와 같은 행에 있거나 적이 있던곳이거나 사거리보다 멀리있으면 continue
                if ei >= ax or a_copy[ei][ej] == 0 or distance > d: 
                    continue
                
                heapq.heappush(heap, (distance, ej, ei))

            if heap:
                dis, y, x = heapq.heappop(heap)
                temp.append((x, y))
                
        # 적 공격
        for tx, ty in temp:
            # 같은 적을 볼 수 있으므로 1일때만 count
            if a_copy[tx][ty]: cnt += 1
            a_copy[tx][ty] = 0

    return cnt

def BACK(depth, idx):
    global n, m, ans
    # 모든 궁수를 배치했다면
    if depth == 3:
        ans = max(ans, START())
        return 
    
    for i in range(idx, m):
        # 궁수 배치
        archer[depth][1] = i
        BACK(depth + 1, i + 1)

BACK(0, 0)
print(ans)
