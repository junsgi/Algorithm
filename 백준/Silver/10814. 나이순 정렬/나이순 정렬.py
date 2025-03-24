n = int(input())
arr = []
for _ in range(n):
    a, b= input().split()
    arr.append([int(a), b, _])
for i in sorted(arr, key=lambda x : (x[0], x[2])):
    print(*i[:-1])