import sys
n = int(sys.stdin.readline().strip())
ans = 0
n = 1000 - n
ans += n // 500
n = n % 500

ans += n // 100
n = n % 100

ans += n // 50
n = n % 50

ans += n // 10
n = n % 10

ans += n // 5
n = n % 5

ans += n
print(ans)