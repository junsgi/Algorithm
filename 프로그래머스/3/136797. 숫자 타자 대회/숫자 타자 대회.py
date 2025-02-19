from sys import setrecursionlimit as s
s(100_100)

def memo(left, right, depth, n, freq, DP):
    if depth == len(n):
        return 0
    if freq[depth][left][right] != 99_999_999:
        return freq[depth][left][right]
    res1 = 99_999_999
    res2 = 99_999_999
    if n[depth] != right:
        res1 = memo(n[depth], right, depth + 1, n, freq, DP) + DP[left][n[depth]]
    if n[depth] != left:
        res2 = memo(left, n[depth], depth + 1, n, freq, DP) + DP[right][n[depth]]
        
    freq[depth][left][right] = min(res1, res2)
    return min(res1, res2)
def solution(numbers):
    answer = 0
    DP = [[99_999_999] * 10 for _ in range(10)]
    freq = [[[99_999_999] * 10 for _ in range(10)] for __ in range(len(numbers))]
    d = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
    key = lambda x, y : x * 3 + y + 1 if x * 3 + y != 10 else 0
    for i in range(4):
        for j in range(3):
            if i == 3 and not (j & 1): continue
            for k in range(8):
                tx = i + d[k][0]
                ty = j + d[k][1]
                if not (0 <= tx < 4 and 0 <= ty < 3): continue
                if tx == 3 and not(ty & 1): continue
                if k & 1: DP[key(i, j)][key(tx, ty)] = 2
                else: DP[key(i, j)][key(tx, ty)] = 3
    for k in range(10):
        for i in range(10):
            for j in range(10):
                if i == j: continue
                DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])
    for i in range(10):
        DP[i][i] = 1
    numbers = list(map(int, numbers))
    return memo(4, 6, 0, numbers, freq, DP)