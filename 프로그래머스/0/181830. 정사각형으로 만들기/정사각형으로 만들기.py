def solution(arr):
    answer = [[]]
    N, M = len(arr), len(arr[0])
    if N == M: 
        return arr
    if N < M:
        diff = abs(N - M)
        for i in range(diff):
            arr.append([0] * M)
    else:
        diff = abs(N - M)
        for i in range(N):
            arr[i].extend([0] * diff)
    return arr