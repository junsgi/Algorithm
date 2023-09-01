check = [0] * 1001
for i in range(4, 1001, 2): check[i] = 1

for i in range(3, 1001, 2):
    swi = 0
    for j in range(2, i):
        if i * i < j or  i % j == 0: 
            swi = 1
            break
    if not swi:
        for j in range(i + i, 1001, i):
            check[j] = 1

n, m = map(int, input().split())
a = list(map(int, input().split()))
cow = [0] * m
a.sort()
result = set()
def rec(depth, idx):
    global n
    if depth == m:
        ans = sum(cow)
        if ans > 1000: return
        if not check[ans]:
            result.add(str(ans))
        return
    
    for i in range(idx, n):
        cow[depth] = a[i]
        rec(depth + 1, i + 1)
rec(0, 0)
if result:
    print(" ".join(sorted(list(result))))
else:
    print(-1)