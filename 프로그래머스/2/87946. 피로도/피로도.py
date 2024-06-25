def p(depth, k, d, ck):
    if ck == (1 <<  len(d)) - 1:
        return depth
    answer = -1
    for i in range(len(d)):
        if ck & (1 << i): continue
        if d[i][0] > k :
            answer = max(answer, p(depth, k, d, ck | (1 << i)))
        else:
            answer = max(answer, p(depth + 1, k - d[i][1], d, ck | (1 << i)))
            
    return answer
        
def solution(k, dungeons):
    return p(0, k, dungeons, 0)