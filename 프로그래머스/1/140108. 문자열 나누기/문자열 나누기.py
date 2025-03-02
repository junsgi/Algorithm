def solution(s):
    answer = 0
    while s:
        answer += 1
        x = s[0]
        a, b = 0, 0
        for i in range(len(s)):
            if s[i] == x:
                a += 1
            else:
                b += 1
            if a == b:
                s = s[i + 1:]
                break
        else:
            break
    return answer