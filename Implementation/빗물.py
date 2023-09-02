n, m = map(int, input().split())
a = list(map(int, input().split()))
rain = [[0] * (m + 1) for i in range(n + 1)]
for idx, value in enumerate(a, 1):
    for i in range(value):
        rain[i][idx] = 1
ans = 0
for row in rain:
    # 첫 번째 벽 초기화
    swi = 0
    for i in range(1, m + 1):
        
        if row[i]: # 벽을 찾았으면

            # 첫 번째 벽이 존재한다면 빗물 개수 구함
            if swi:
                ans += len(row[swi + 1 : i])
            
            swi = i
print(ans)