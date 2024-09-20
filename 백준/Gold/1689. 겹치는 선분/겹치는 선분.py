import sys
input = sys.stdin.readline
arr = []
for _ in range(int(input().strip())):
    s, e = map(int, input().split())
    arr.append((s, 1))
    arr.append((e, -1))
arr.sort()
answer = 0
p = 1
for _, t in arr[1:]:
    answer = max(answer, p)
    p += t
print(answer)