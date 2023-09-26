# https://www.acmicpc.net/problem/17143
import sys
input = sys.stdin.readline
N, M, S = map(int, input().split())
graph = [[0] * (M + 1) for _ in range(N + 1)]
sharks = []
for _ in range(S):
    r, c, s, d, z = map(int, input().split())
    sharks.append([r, c, s, d, z, 1 if d == 2 or d == 3 else -1])

dire = [0, [-1, 0], [1, 0], [0, 1], [0, -1]]
chain = [0, 2, 1, 4, 3]
getCost = [0, 1, N,  M, 1]
move = [0, N - 1, N - 1, M - 1, M - 1]
end = [0, [N, None], [1, None], [None, 1], [None, M]]
ans = 0

def MOVE(sharks):
    global N, M
    for i in range(len(sharks)):
        row, col, speed, d, size, pm = sharks[i]
        cost = abs((row if d == 1 or d == 2 else col) - getCost[d])

        if speed <= cost:
            sharks[i][0] = row + speed * dire[d][0]
            sharks[i][1] = col + speed * dire[d][1]
        else:
            speed -= cost
            d = chain[d]
            pm = -pm
            ck = speed // move[d]
            sharks[i][0] = end[d][0] if end[d][0] else row
            sharks[i][1] = end[d][1] if end[d][1] else col

            if ck % 2 == 0:
                sharks[i][0] += ((speed % move[d]) * dire[d][0]) 
                sharks[i][1] += ((speed % move[d]) * dire[d][1])
            else:
                sharks[i][0] = end[chain[d]][0] if end[chain[d]][0] else row
                sharks[i][1] = end[chain[d]][1] if end[chain[d]][1] else col
                pm = -pm
                sharks[i][0] += ((speed % move[d]) * dire[d][0]) * pm
                sharks[i][1] += ((speed % move[d]) * dire[d][1]) * pm

        
        if d == 1 and sharks[i][0] == 1:
            d = chain[d]
        if d == 2 and sharks[i][0] == N:
            d = chain[d]
        if d == 3 and sharks[i][1] == M:
            d = chain[d]
        if d == 4 and sharks[i][1] == 1:
            d = chain[d]
        sharks[i][5] = pm
        sharks[i][3] = d


def EAT(sharks):
    sharks.sort(key = lambda x : (x[0], x[1], -x[4]))
    result = []
    maxidx = -1
    for i in range(len(sharks) - 1):
        print(*sharks[i])
        


"""
r, c : 상어 위치
s : 속력 (탐색 깊이)
d : 이동방향
z : 크기 (위치가 겹친다면 가장 큰 상어가 나머지 다 잡아먹음)
"""

for i in range(1, M + 1):
    # 낚시왕이 오른쪽으로 한 칸 이동한다.

    # 낚시왕이 있는 열에 있는 상어 중 가장 가까운 상어를 잡는다.
    idx = -1
    col = -1
    for j in range(len(sharks)):
        if sharks[j][1] == i:
            if idx == -1 or col > sharks[j][0]:
                col = sharks[j][0]
                idx = j
    if idx != -1:
        ans += sharks[idx][4]
        del sharks[idx]


    # 상어가 이동한다.
    # 모든 상어가 속력 만큼 이동
    MOVE(sharks)
    print(sharks)

    # 좌표가 겹친다면 크기가 큰 상어를 제외하고 모두 잡아먹는다.
    EAT(sharks)
print(ans)