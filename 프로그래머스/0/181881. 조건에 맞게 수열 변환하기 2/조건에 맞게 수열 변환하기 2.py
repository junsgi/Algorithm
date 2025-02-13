def solution(arr):
    answer = 0
    hit = 1
    while hit:
        hit = 0
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] & 1 == 0:
                arr[i] //= 2
                hit = 1
            elif arr[i] < 50 and arr[i] & 1:
                arr[i] = arr[i] * 2 + 1
                hit = 1
        answer += 1
    return answer - 1