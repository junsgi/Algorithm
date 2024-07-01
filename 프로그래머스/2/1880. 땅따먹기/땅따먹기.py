def solution(land):
    answer = 0
    for i in range(len(land) - 2, -1, -1):
        for a in range(4):
            MAX = 0
            for b in range(4):
                if a == b: continue
                MAX = max(MAX, land[i + 1][b])
            land[i][a] += MAX
    return max(land[0])