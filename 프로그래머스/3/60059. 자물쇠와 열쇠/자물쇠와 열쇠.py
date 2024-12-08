
"""
AI CNN 알고리즘을 참고함.
(lock -> input, Key를 -> filter)
key 한 변의 길이 = N
lock 한 변의 길이 = M
[key][lock][key] -> 겹쳐야 하므로 N + M + N에서 2를 뺀다.
padding size = N + M * 2 - 2

key 범위 = (0, 0), (N + M * 2 - 2, N + M * 2 - 2)
lock 범위 = (N - 1, N - 1), (N + M - 2, N + M - 2)


N = 3
90
(x, y) -> (y, N - x - 1)
(1, 0) -> (0, 1)
(2, 1) -> (1, 0)
(2, 2) -> (2, 0)


180
(x, y) -> (N - x - 1, N - y - 1)
(1, 0) -> (1, 2)
(2, 1) -> (0, 1)
(2, 2) -> (0, 0)

270
(x, y) -> (N - y - 1, x)
(1, 0) -> (2, 1)
(2, 1) -> (1, 2)
(2, 2) -> (0, 2)
"""
from copy import deepcopy
def solution(key, lock):
    N, M = len(key), len(lock)
    keys = []
    locks = []
    for i in range(N):
        for j in range(N):
            if key[i][j]:
                keys.append([i, j])
    for i in range(M):
        for j in range(M):
            if not lock[i][j]:
                locks.append([i + N - 1, j + N - 1])
    def t90(arr):
        return [[b, N - a - 1] for a, b in arr]
    def t180(arr):
        return [[N - a - 1, N - b - 1] for a, b in arr]
    def t270(arr):
        return [[N - b - 1, a] for a, b in arr]
    def check(arr):
        if len(arr) < len(locks):
            return False
        c = 0
        for i in arr:
            if i in locks: c += 1
            # 열쇠가 자물쇠 돌기에 부딪힌 경우 처리
            # lock 범위 = (N - 1, N - 1), (N + M - 2, N + M - 2)
            elif (N - 1) <= i[0] <= (N + M - 2) and (N - 1) <= i[1] <= (N + M - 2):
                return False
        if len(locks) == c:
            return True
        return False
    def move(arr):
        for i in range(N + M - 1): # X축
            temp = deepcopy(arr)
            for j in range(len(arr)):
                temp[j][0] = arr[j][0] + i
            for j in range(N + M - 1): # Y축
                for k in range(len(arr)):
                    temp[k][1] = arr[k][1] + j
                if check(temp): return True
        return False
    if move(keys): return True
    t = t90(keys)
    if move(t): return True

    t = t180(keys)
    if move(t): return True

    t = t270(keys)
    if move(t): return True
    return False
