n = int(input())
plus = list(map(int, input().split()))
minus = list(map(int, input().split()))
K = list(map(float, input().split()))
ans = 0
for i in range(n):
    case1 = int((plus[i] * 10) * (K[i] * 10) / 100) - minus[i]
    case2 = int((-minus[i] * 10) * (K[i] * 10) / 100) + plus[i] 
    ans += max(case1, case2)
print(ans)