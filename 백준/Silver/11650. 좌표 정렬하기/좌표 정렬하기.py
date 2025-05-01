from heapq import heappush, heappop
h=[]
for _ in range(int(input())):
    heappush(h, tuple(map(int, input().split())))
while h:
    print(*heappop(h))