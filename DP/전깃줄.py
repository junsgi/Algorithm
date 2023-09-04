n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
a.sort(key = lambda x : x[0])
DP = [-1] * n
# 가장 처음엔 하나만 연결
DP[0] = 1
ans = 0
for i in range(1, n):
    cnt = 0
    # 현재 선 연결
    DP[i] = 1

    for j in range(i - 1, -1, -1):
        # 겹치는 줄이 없다면 DP 배열에 겹치지 않으면서 
        # 연결했을 때 가장 많이 연결할 수 있는 선의 개수가 저장
        if (a[i][0] > a[j][0] and a[i][1] > a[j][1]):
            cnt = max(DP[j], cnt)


    # 만약 cnt가 0이라면 모든 줄과 겹치므로 0임
    DP[i] += cnt
    ans = max(DP[i], ans)
print(n - ans)

# 현재 줄과 겹치지 않으면서 가장 많이 연결할 수 있는 선의 개수