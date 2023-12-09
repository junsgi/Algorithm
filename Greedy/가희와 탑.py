# https://www.acmicpc.net/problem/24337
n, a, b = map(int, input().split())
if n + 1 < a + b:
    print(-1)
    exit()
arr = [1] * n
# b를 기준으로 건물 세움
for i in range(b):
    arr[i] = i + 1
arr.reverse()
if a != 1:
    # a가 보고싶은 건물의 시작 인덱스 구함 (1은 최대한 왼쪽으로 붙여야하기 때문)
    # n - b : 전체 길이에서 b가 보고싶은 건물은 구했으므로 시작 인덱스를 줄인다.
    # n - b - a : b가 볼 수 있는 가장 멀리있는 건물에서 a가 보고싶은 건물의 개수 만큼 더 인덱스를 줄인다.
    # n - b - a + 1: a가 보고싶은 개수만큼 줄이면 보고싶은 개수보다 하나 더 보게 되므로 1을 더한다.
    st = n - b - a + 1
    for i in range(st, st + a):
        if arr[i] > i - st + 1:break
        arr[i] = i - st + 1
    print(*arr)
else:
    arr.insert(0, arr.pop(n - b))
    print(*arr)  