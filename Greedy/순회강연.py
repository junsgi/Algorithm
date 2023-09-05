# https://www.acmicpc.net/problem/2109


n =int(input())
a = [list(map(int, input().split())) for i in range(n)]
a.sort(key = lambda x : -x[0])
print(a)

# i일에 벌 수 있는 최대값 저장
check = [0] * 10001

# n일 안에 강연을 한다면 최대 n번 할 수 있기 때문에 넘어가진 않는지 체크
cnt = [0] * 10001

for i in range(n):
    pay, day = a[i][0], a[i][1]

    if check[day] == 0:
        check[day] = pay
        cnt[day] += 1
    else:
        # n일만큼 했다면
        if cnt[day] == day: continue

        for j in range(day - 1, 0 , -1):
            # 일찍 부르지만 페이는 낮은경우
            if check[j] < pay:
                check[j] = pay
                cnt[day] += 1
                break
            # j날짜가 비어있는 경우
            if not check[j]:
                check[j] = pay
                break
print(sum(check))