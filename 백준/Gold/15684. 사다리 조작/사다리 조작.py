import sys
input = sys.stdin.readline
n, m, h = map(int, input().strip().split())
arr = [[0 for i in range(n + 2)] for j in range(h + 1)]
ans = 0
for i in range(m):
    x, y = map(int, input().strip().split())
    arr[x][y] = 1

def move():
    global n, h
    sdr = 0
    for t in range(1, n + 1):
        sdr = t
        for x in range(1, h + 1):
            if arr[x][sdr]: sdr+=1
            elif arr[x][sdr-1]: sdr -= 1
        if sdr != t: return False
    return True

def back(cnt, col, row):
    global ans
    if cnt == ans:
        if move():
            print(ans)
            exit()
        return
    for y in range(col, n):
        for x in range(row, h + 1):
            if arr[x][y - 1] + arr[x][y] + arr[x][y + 1]: continue
            arr[x][y] = 1
            back(cnt + 1, col, x + 1)
            arr[x][y] = 0
        row = 1

for i in range(4):
    ans = i
    back(0, 1, 1)
print(-1)