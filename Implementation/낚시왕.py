# https://www.acmicpc.net/problem/17143
import sys
input = sys.stdin.readline
dire = [0, [-1, 0], [1, 0], [0, 1], [0, -1]]
dire2 = [0, -1, 1, 1, -1]
ans = 0
def MOVE(sharks):
    pass

def EAT(sharks):
    pass

"""
r, c : 상어 위치
s : 속력 (탐색 깊이)
d : 이동방향
z : 크기 (위치가 겹친다면 가장 큰 상어가 나머지 다 잡아먹음)
"""
N, M, S = map(int, input().split())
graph = [[0] * (M + 1) for _ in range(N + 1)]
sharks = []
for _ in range(S):
    r, c, s, d, z = map(int, input().split())
    sharks.append((r, c, s, d, z, dire2[d]))

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

    # 좌표가 겹친다면 크기가 큰 상어를 제외하고 모두 잡아먹는다.
    EAT(sharks)

    # continue
    print(sharks)
    exit()