# https://www.acmicpc.net/problem/2141
n = int(input())
arr = []
allPeople = 0
for _ in range(n):
    v, p = map(int, input().split())
    allPeople += p
    arr.append([v, p])
arr.sort(key = lambda x : (x[0], x[1]))
s = 0
for v, p in arr:
    s += p
    if s >= allPeople // 2 + 1:
        print(v)
        break