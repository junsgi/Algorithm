from collections import defaultdict
from heapq import heappush, heappop
def solution(genres, plays):
    answer = []
    dic = defaultdict(list)
    for i in range(len(plays)):
        heappush(dic[genres[i]], (-plays[i], i))
    result = list(dic.items())
    for i in range(len(result)):
        n, a = result[i]
        S = sum(map(lambda x : -x[0], a))
        result[i] = (n, a, S)
    result.sort(key = lambda x : (-x[2]))
    for n, a, s in result:
        for i in range(2):
            if a: answer.append(heappop(a)[1])
    return answer