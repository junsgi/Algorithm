def solution(arr, k):
    return list(map(lambda x : x * k if k % 2 else x + k, arr))