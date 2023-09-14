# https://www.acmicpc.net/problem/1036
alpha = { int(chr(x), 36) : chr(x)  for x in range(65, 91) }
for i in range(10): 
    alpha[i] = i
print(alpha)

MAX = [0] * 37
n = int(input())
words = [input() for _ in range(n)]
k = int(input())
a = {}

for w in words:
    tnum = 1
    for j in range(len(w) - 1, -1, -1):
        if w[j] in a:
            a[w[j]] += int(w[j], 36) * tnum
        else:
            a[w[j]] = int(w[j], 36) * tnum
        if w[j] != 'Z':
            MAX[int(w[j], 36)] += 35 * tnum
        tnum *= 10
        
MAX.sort(reverse=True)
a = sorted(a.values(), reverse = True)
ans = 0
for i in range(len(a)):
    if k:
       ans += MAX[i]
       k -= 1
    else:
        ans += a[i]
print(MAX[:len(a)])
print(a)
print(ans)
while ans :
    print(alpha[ans % 36])
    ans //= 36