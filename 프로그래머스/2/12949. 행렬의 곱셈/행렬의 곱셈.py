def solution(arr1, arr2):
    N, M = len(arr1), len(arr2[0])
    answer = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            res = 0
            for x in range(len(arr1[i])):
                res += arr1[i][x] * arr2[x][j]
            answer[i][j] = res
    return answer