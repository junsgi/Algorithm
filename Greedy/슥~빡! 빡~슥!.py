n = int(input())
plus = list(map(int, input().split()))
minus = list(map(int, input().split()))
K = list(map(float, input().split()))
ans = 0

# 소수점 계산에 문제가 있어 최대한 정수로 형변환하여 풀었다.

for i in range(n):
    # Ai * Ki - 회피
    case1 = int((plus[i] * 10) * int(K[i] * 10) / 100) - minus[i]

    # -Bi * Ki + 공격
    case2 = int((-minus[i] * 10) * int(K[i] * 10) / 100) + plus[i] 

    ans += max(case1, case2)
print(ans)