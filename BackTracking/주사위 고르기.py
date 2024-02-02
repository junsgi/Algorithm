# https://school.programmers.co.kr/learn/courses/30/lessons/258709
import math
CNT = 0
MAX = 0
answer = []
def BACK(depth, idx, N, A, dice, LIMIT):
    global CNT, MAX, answer
    if depth == N // 2:
        CNT += 1
        B = [i for i in range(N) if i not in A]
        T = 0
        F = 0
        # for a in A:
        #     for b in B:
        #         print(a, dice[a], b, dice[b])
        #         for x in dice[a]:
        #             for y in dice[b]:
        #                 if x < y : F += 1
        #                 elif x > y : T += 1
        print(A, B, T, F)
        print(T, F)
        if MAX < T:
            MAX = T
            answer = list(A)
        if MAX < F:
            MAX = F
            answer = list(B)
        return
    
    for i in range(idx, N):
        if CNT == LIMIT: return
        BACK(depth + 1, i + 1, N, A + [i], dice, LIMIT)


def solution(dice):
    LEN = len(dice)
    LIMIT = math.comb(LEN, LEN // 2)
    BACK(0, 0, LEN, [], dice, LIMIT // 2)
    for i in range(LEN // 2):
        answer[i] += 1
    print(answer)
    return answer

"""
2 -> 2
4 -> 6
6 -> 20
8 -> 70
10 ->252
"""
solution(
    [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]],
    # [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]],
    # [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
)