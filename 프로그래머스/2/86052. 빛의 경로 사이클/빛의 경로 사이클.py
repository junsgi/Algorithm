import sys
sys.setrecursionlimit(500 * 500 * 10)
def solution(grid):
    answer = []
    N, M = len(grid), len(grid[0])
    DP = [[[-1 for _ in range(M)] for __ in range(N)] for ___ in range(4)]
    dire = ((-1, 0), (1, 0), (0, -1), (0, 1))
    def memo(x, y, z, depth, cnt):
        nonlocal DP, N, M, grid, dire
        if x >= N: x = 0
        if y >= M: y = 0
        if x < 0: x = N - 1
        if y < 0: y = M - 1
        if DP[z][x][y] == cnt:
            return depth
        if DP[z][x][y] != -1:
            return 0
        DP[z][x][y] = cnt
        if grid[x][y] == "S":
            z = z
        elif z == 3:
            if grid[x][y] == "L":
                z = 0
            else:
                z = 1
        elif z == 2:
            if grid[x][y] == "L":
                z = 1
            else:
                z = 0
        elif z == 1:
            if grid[x][y] == "L":
                z = 3
            else:
                z = 2
        elif z == 0:
            if grid[x][y] == "L":
                z = 2
            else:
                z = 3
        res = memo(x + dire[z][0], y + dire[z][1], z, depth + 1, cnt)
        if res == 0: DP[z][x][y] = -1
        return res
        
    cnt = 1
    for i in range(N):
        for j in range(M):
            for k in range(4):
                ans = memo(i, j, k, 1, cnt)
                cnt += 1
                if ans != 0: 
                    answer.append(ans - 1)
    answer.sort()
    return answer

"""
상 : 0
하 : 1
좌 : 2
우 : 3
방향 문자 새방향
4   L   1 
4   R   2 

3   L   2 
3   R   1 

1   L   3 
1   R   4 

2   L   4 
2   R   3 

LL
LL
"""
