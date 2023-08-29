import sys
input = sys.stdin.readline
n = int(input().strip())
p = []
m = []
z = False
for _ in range(n):
    num = int(input().strip())
    if num > 0:
        p.append(num)
    elif num < 0:
        m.append(num)
    else:
        z = True

p.sort(reverse=True)
t1 = 0
for i in range(1, len(p), 2):
    t1 += max(p[i] * p[i-1], p[i] + p[i-1])

if len(p) % 2:
    t1 += p[len(p) - 1]

t2 = 0
if len(m) == 1:
    if z:
        print(t1)
    else:
        print(t1 + m[0])
else:
    m.sort()
    for i in range(1, len(m), 2):
        t2 += m[i] * m[i-1]
    
    if len(m) % 2:
        if z:
            print(t1 + t2)
        else:
            print(t1 + t2 + m[len(m) - 1])
    else:
        print(t1 + t2)
