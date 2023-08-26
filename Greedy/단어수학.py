import sys
input = sys.stdin.readline
n = int(input().strip())
che = {}
k = 1
for i in range(n):
    word = input().strip()
    k = 1
    for w in word[::-1]:
        if w in che:
            che[w] += k
        else:
            che[w] = k
        k *= 10

k = 9
ans = 0
for key, value in sorted(che.items(), key = lambda x : -x[1]):
    ans += value * k
    k -= 1
print(ans)