def solution(clothes):
    answer = 1
    dic = {}
    for i, j in clothes:
        if j not in dic:
            dic[j] = 2
        else:
            dic[j] += 1
            
    for k in dic.keys():
        answer *= dic[k]
    return answer - 1