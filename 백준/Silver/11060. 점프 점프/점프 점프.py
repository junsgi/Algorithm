import sys
MAX = 0x7fffffff
input = sys.stdin.readline
def p(depth, idx, arr):
    global DP, MAX
    if idx == len(arr) - 1:
        DP[depth][idx] = min(DP[depth][idx], depth)
        return DP[depth][idx]
    
    if DP[depth][idx] != MAX:
        return DP[depth][idx]
    for i in range(1, arr[idx] + 1):
        if idx + i >= len(arr): continue
        DP[depth][idx] = min(DP[depth][idx], p(depth + 1, idx + i, arr))
    return DP[depth][idx]
n = int(input())
arr = tuple(map(int, input().split()))
DP = [[MAX] * n for _ in range(n)]
answer = p(0, 0, arr)
if answer == MAX:
    print(-1)
else:
    print(answer)
