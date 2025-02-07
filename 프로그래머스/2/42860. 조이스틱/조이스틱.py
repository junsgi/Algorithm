def solution(name):
    answer = 0
    loc = 0
    cnt = 0x7fffffff
    for i in range(len(name)):
        answer += min(ord(name[i]) - 65, 91 - ord(name[i]))
        if name[i] == 'A': continue
        if i == 0: continue
        tmp = loc + len(name) - i # 이전 위치에서 남은 문자 개수
        cnt = min(cnt, min(loc + tmp, tmp + len(name) - i))
        loc = i
    cnt = min(cnt, loc)
    return answer + cnt