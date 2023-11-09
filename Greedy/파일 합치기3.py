# https://www.acmicpc.net/problem/13975
from heapq import heappush, heappop, heapify
n = int(input())

def f(arr):
    result = 0
    for _ in range(len(arr) - 1):
        t1 = heappop(arr)
        result += t1
        t2 = heappop(arr)
        result += t2
        heappush(arr, t1 + t2)
    return result

for _ in range(n):
    LEN = int(input())
    arr = list(map(int, input().split()))
    heapify(arr)
    print(f(arr))

"""
크기가 큰 파일은 가장 작은 파일과 합쳐서 답을 구하려고 했지만
나중에 크기가 더욱 커진 파일과 계산을 해야하는 경우가 나와 제대로된 답이 나오지 않았다.

해결방법은 크기가 작은 파일끼리 최대한 합치는 것이다.
5개 파일은 4번의 합치는 과정이 있고
6개의 파일은 5번의 합치는 과정이 있기 때문에
배열의 길이 - 1 만큼만 수행한다.
"""