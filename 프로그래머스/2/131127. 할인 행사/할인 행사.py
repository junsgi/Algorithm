def solution(want, number, discount):
    answer = 0
    check = {}
    for i in range(len(want)):
        check[want[i]] = number[i]
    for i in range(len(discount) - 9):
        dic = {}
        for j in range(i, i + 10):
            if discount[j] in check:
                if discount[j] in dic:
                    dic[discount[j]] += 1
                else:
                    dic[discount[j]] = 1
        if len(dic) == len(check):
            for key, value in dic.items():
                if check[key] != value:
                    break
            else:
                answer += 1
            
    return answer