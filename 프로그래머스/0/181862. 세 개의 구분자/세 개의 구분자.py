def solution(myStr):
    s = ""
    answer = []
    for i in myStr:
        if i == 'a' or i == 'b' or i == 'c':
            if s: answer.append(s)
            s = ""
        else:
            s += i
    if s:
        answer.append(s)
    if not answer: answer.append("EMPTY")
    return answer