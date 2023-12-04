n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
arr.sort(key = lambda x : (x[0], -x[1]))

for i in range(n):
    weight, value = arr[i]

    cur = m - weight
    cost = value
    m1 = 0
    w1 = 0
    for j in range(i + 1, n):
        pass
    
"""
3 9
3 7
3 2
4 10
4 9
7 100
7 1
"""