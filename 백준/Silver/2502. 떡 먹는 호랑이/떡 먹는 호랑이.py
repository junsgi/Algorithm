n, m = map(int, input().split())
for i in range(1, m):
    for j in range(1, m):
        DP = [i, j]
        for _ in range(n - 2):
            DP.append(DP[-1] + DP[-2])
        
        if DP[-1] == m:
            print(i, j, sep = "\n")
            exit()