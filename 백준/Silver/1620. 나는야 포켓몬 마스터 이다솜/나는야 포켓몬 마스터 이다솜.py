n, m = map(int, input().split())
arr = [0]
dic = {}
for i in range(1, n + 1):
    s = input()
    arr.append(s)
    dic[s] = i
for _ in range(m):
    q = input()
    if q.isdigit():
        print(arr[int(q)])
    else:
        print(dic[q])