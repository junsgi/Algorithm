import sys
t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    comp = []
    freq = [0] * (n + 1)
    for __ in range(n):
        comp.append(list(map(int, sys.stdin.readline().strip().split())))
    
    comp.sort(key = lambda x : x[0])
    cnt = 1
    st = comp[0]
    for i in range(1, n):
        if st[1] > comp[i][1]:
            cnt += 1
            st = comp[i]
    print(cnt)