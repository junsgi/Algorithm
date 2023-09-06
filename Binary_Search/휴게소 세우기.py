# https://www.acmicpc.net/problem/1477

"""
배열 첫 번째는 고속도로 시작을 뜻하는 0
마지막엔 고속도로 끝부분과 편의점 거리를 구해야하므로 l append

편의점 사이의 거리를 mid로
m개보다 많이 설치해야된다면 편의점 거리를 줄여 m개에 맞춤
"""
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