# https://www.acmicpc.net/problem/7453
import sys
input = sys.stdin.readline
n = int(input())
arr = [[], [], [], []]
A, B = [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    arr[0].append(a)
    arr[1].append(b)
    arr[2].append(c)
    arr[3].append(d)
dic = {}
for i in arr[0]:
    for j in arr[1]:
        if i + j in dic:
            dic[i + j] += 1
        else:
            dic[i + j] = 1
cnt = 0
for i in arr[2]:
    for j in arr[3]:
        if -(i + j) in dic:
            cnt += dic[-(i + j)]
print(cnt)