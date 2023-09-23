# https://www.acmicpc.net/problem/17143
import sys
input = sys.stdin.readline
dire = [0, [-1, 0], [1, 0], [0, 1], [0, -1]]
fishman = [0, 0]
ans = 0
"""
r, c : 상어 위치
s : 속력 (탐색 깊이)
d : 이동방향
z : 크기 (위치가 겹친다면 가장 큰 상어가 나머지 다 잡아먹음 (같으면 안먹는듯?))
"""
N, M, S = map(int, input().split())
graph = [[0] * (M + 1) for _ in range(N + 1)]
sharks = []
for _ in range(S):
    r, c, s, d, z = map(int, input().split())
    sharks.append((r, c, s, d, z))