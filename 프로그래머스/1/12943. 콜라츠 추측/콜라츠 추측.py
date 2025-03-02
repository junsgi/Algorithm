def solution(num):
    answer = 0
    while answer != 500:
        if num == 1:
            return answer
        if num&1:num=num*3+1
        else:num//=2
        answer += 1
    return -1