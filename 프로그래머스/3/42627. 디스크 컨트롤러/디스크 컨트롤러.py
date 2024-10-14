import math
def up(idx, heap, time):
    if idx // 2 == 0: return
    p = heap[idx // 2][0] if heap[idx // 2][0] - time > 0 else 0
    c = heap[idx][0] if heap[idx][0] - time > 0 else 0
    if p > c or (p == c and heap[idx][1] < heap[idx // 2][1]):
        heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
        up(idx // 2, heap, time)
    
def down(idx, heap, time):
    c = idx * 2
    if c >= len(heap): return
    if c + 1 < len(heap):
        c1 = heap[c][0] if heap[c][0] - time > 0 else 0
        c2 = heap[c + 1][0] if heap[c + 1][0] - time > 0 else 0
        if c1 > c2 or (c1 == c2 and heap[c][1] > heap[c + 1][1]):
            c += 1
    p = heap[idx][0] if heap[idx][0] - time > 0 else 0
    child = heap[c][0] if heap[c][0] - time > 0 else 0
    if p > child or (p == child and heap[idx][1] > heap[c][1]):
        heap[idx], heap[c] = heap[c], heap[idx]
        down(c, heap, time)
    
            
def solution(jobs):
    answer = 0
    time = 0
    heap = [None]
    visit = [0] * len(jobs)
    for i in range(len(jobs)):
        heap.append((jobs[i][0], jobs[i][1], i))
        up(len(heap) - 1, heap, time)
        
    while len(heap) != 1:
        job = heap[1]
        if time < job[0]: time = job[0]
        visit[job[2]] = 1
        heap[1] = heap[-1]
        heap.pop()
        down(1, heap, time)
        t = 0 if time - job[0] < 0 else time - job[0]
        answer += t + job[1]
        time += job[1]
        
        temp = [None]
        for i in range(len(jobs)):
            if visit[i]: continue
            temp.append((jobs[i][0], jobs[i][1], i))
            up(len(temp) - 1, temp, time)
        heap = temp
    return math.floor(answer // len(jobs))