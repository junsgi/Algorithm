from heapq import heappush, heappop, heapify
n, m = map(int, input().split())
heap = list(map(int, input().split()))
heapify(heap)

    
for _ in range(m):
    t1 = heappop(heap)
    t2 = heappop(heap)
    t = t1 + t2
    
    heappush(heap, t)
    heappush(heap, t)
print(sum(heap))