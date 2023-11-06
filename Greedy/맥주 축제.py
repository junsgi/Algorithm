# https://www.acmicpc.net/problem/17503
from heapq import heappush, heappop
n, m, k = map(int, input().split())
heap = []
eat = []

for _ in range(k):
    pre, level = map(int, input().split())
    heappush(heap, (level, -pre))
sum = 0
cnt = 0
before = 0
answer = -1

for _ in range(n):
    t = heappop(heap)
    heappush(eat, (-t[1], t[0]))
    sum += -t[1]
    answer = t[0]

if sum >= m:
    print(answer)
else:
    answer = -1
    for _ in range(k - n):
        e = heappop(eat)
        sum -= e[0]
        t = heappop(heap)
        heappush(eat, (-t[1], t[0]))
        sum += -t[1]

        if sum >= m:
            answer = t[0]
            break
    print(answer)
"""
맥주 도수가 3, 3, 5라면
3개의 맥주를 모두 마실 수 있는 간 레벨의 최소는 5임
ex) 1, 1, 21000000 -> 3개의 맥주를 모두 마실 수 있는 간 레벨은 21000000임

맥주 힙 정렬 우선순위
1. 도수 낮은게 1순위
2. 선호도 높은게 2순위

먹어야 하는 맥주 우선순위
1. 선호도 낮은게 1순위
2. 도수 낮은게 2순위

풀이
1. n번만큼 맥주를 일단 마신다.
2. 만족도를 채우면 가장 마지막에 뽑은 도수 레벨 출력
3. 채우지 못했으면 선호도가 가장 낮은 맥주를 버리고 새로운 맥주를 선택한다.
4. 만족했으면 마지막으로 뽑은 요소의 레벨 출력후 종료
5. 만족 못했으면 3번으로
"""