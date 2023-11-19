# https://school.programmers.co.kr/learn/courses/30/lessons/72416
from heapq import heappush, heappop, heapify
def solution(sales, links):
    answer = 0
    graph = [[] for _ in range(len(sales) + 1)]
    for st, ed in links:
        graph[st].append(ed)
    que = []
    heappush(que, [])
    return answer