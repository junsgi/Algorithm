# https://www.acmicpc.net/problem/1477

n, m, l = map(int, input().split())
a = [0]
a.extend(list(map(int, input().split()))) if n else [0]
a.append(l)
a.sort() if a else a

left = 1
right = l
ans = 0x7fffffff
while left <= right:
    mid = (left + right) // 2
    sum = 0

    for i in range(1, len(a)):
        length = a[i] - a[i - 1] - 1
        if mid <= length:
            sum += length // mid
        if sum > m : break

    if sum > m:
        left = mid + 1
    else:
        ans = min(ans, mid)
        right = mid - 1
print(ans)
"""
200 451 701 800
   251 250 99

200 450 701 800
   250  251 99

200 452 701 800
   252 249 99

200 449 701 800
   249  252 99

1. 최댓값이 최소가 되려면 구간차이가 가장 큰 곳에 최대한 휴게소를 두어야함


"""