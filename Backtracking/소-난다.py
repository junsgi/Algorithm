check = [0] * 10001
visit = [0] * 10001
check[1] = 1
for i in range(4, 10001, 2): check[i] = 1

for i in range(3, 10001, 2):
    swi = 0
    if check[i]: continue
    for j in range(2, i):
        if i * i < j or  i % j == 0: 
            swi = 1
            break
    if not swi:
        for j in range(i + i, 10001, i):
            check[j] = 1
n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = []
def rec(depth, idx, value):
    global n, ans
    if depth == m:
        if not check[value] and not visit[value]:
            visit[value] = 1
            ans.append(value)
        return
    
    for i in range(idx, n):
        rec(depth + 1, i + 1, value + a[i])
rec(0, 0, 0)
if ans:
    print(" ".join(map(str, sorted(ans))))
else:
    print(-1)