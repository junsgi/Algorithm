def solution(rank, attendance):
    for i in range(len(rank)):
        if not attendance[i]: rank[i] = (999, i)
        else: rank[i] = (rank[i], i)
    rank.sort()
    return 10000 * rank[0][1] + 100 * rank[1][1] + rank[2][1]