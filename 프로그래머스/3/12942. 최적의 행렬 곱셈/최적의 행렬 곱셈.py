def solution(matrix_sizes):
    answer = 0
    arr = matrix_sizes
    DP = [[0] * (len(arr) + 1) for _ in range(len(arr))]
    for i in range(len(arr) - 1):
        DP[i][i + 1] = arr[i][0] * arr[i][1] * arr[i + 1][1]
    cnt = len(arr) - 2
    inc = 2
    for i in range(cnt, 0, -1):
        for j in range(i):
            x, y = j, j + inc
            DP[x][y] = 0x7fffffff
            for k in range(x , y ):
                case1 = DP[x][k] + DP[k + 1][y] + arr[x][0] * arr[k][1] * arr[y][1]
                DP[x][y] = min(DP[x][y], case1)
        inc += 1
    return DP[0][-2]