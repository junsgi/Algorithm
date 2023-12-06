n, m = map(int, input().split())
arr = [[]]
for _ in range(n):
    arr.append(list(map(int, input().split())))
DP = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1): # 물건
    for j in range(1, m + 1): # 무게
        if j - arr[i][0] >= 0 : # i번째 물건이 현재 무게보다 같거나 가볍다면
            DP[i][j] = max(DP[i - 1][j], arr[i][1] + DP[i - 1][j - arr[i][0]])
        else:
            DP[i][j] = DP[i - 1][j]
print(DP[n][m])
"""
i : 물건 인덱스
j : 무게

만들 수 있는 무게 < 현재 물건의 무게 -> 현재 물건을 선택하지 않았을 때 최댓값 (DP[i - 1][j])

만들 수 있는 무게 >= 현재 물건의 무게 
 * max( 현재 물건을 선택하지 않았을 때 최댓값 ,   현재 물건을 선택하고 남은 공간의 최대값  )
 * max( DP[i - 1][j]                      ,    arr[i][1] + DP[i - 1][j - arr[i][0]]  )
"""