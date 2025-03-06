def solution(n, q, ans):
    answer = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                for l in range(k + 1, n + 1):
                    for m in range(l + 1, n + 1):
                        tmp = [i, j, k, l, m]
                        tns = [0] * len(ans)
                        for x in range(len(q)):
                            for y in q[x]:
                                if y in tmp:
                                    tns[x] += 1
                            
                            if tns[x] != ans[x]:
                                break
                        else:
                            answer += 1
    return answer
