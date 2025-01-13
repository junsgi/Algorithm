def p(depth, idx, N, M, arr):
    if depth == 0:
        return [tuple(arr)]
    result = []
    for i in range(idx, M):
        res = p(depth - 1, i + 1, N, M, arr + [i])
        for j in res:
            result.append(j)
    return result
def solution(relation):
    answer = 0
    N, M = len(relation), len(relation[0])
    arr = []
    for i in range(1, M + 1):
        for j in p(i, 0, N, M, []):
            arr.append(j)
    key = set()
    for i in arr:
        for j in key:
            flag = False
            cnt = 0
            for k in i: # 조합
                for c in j: # 최소성 체크
                    if c == k:
                        cnt += 1
                        break
            if cnt == len(j): # 최소성을 만족하지 못하면
                break
        else:
            temp = set()
            for j in range(N):
                t = ""
                for k in i:
                    t += relation[j][k] + " "
                temp.add(t)
            if len(temp) == N:
                key.add(i)
    return len(key)