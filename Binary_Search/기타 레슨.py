n, m = map(int, input().split())
a = list(map(int, input().split()))

le = 1
ri = 1_000_000_000
mid = 0
ans = 0

while le <= ri:
    mid = (le + ri) // 2
    sum = 0
    cnt = 0

    for time in a:
        # 강의가 한 블루레이에 저장 못한다면
        if time > mid : 
            cnt = -1
            break
        
        sum += time
        # 강의 시간이 블루레이 크기를 넘기면
        if sum >= mid:
            cnt += 1

            # 딱 맞았다면 sum 초기화
            if sum == mid:
                sum = 0
            else: # 
                sum = time
        # 강토가 가지고 있는 개수보다 많이 필요하다면 탈출
        if cnt > m :
            break

    # 모든 강의를 저장하긴 했지만 마지막 강의를 포함시키지 않았을 때 실행
    if cnt != -1 and sum != 0 : cnt += 1

    if 0 < cnt <= m:
        ri = mid - 1
        ans = mid
    else:
        le = mid + 1
print(ans)