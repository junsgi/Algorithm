def solution(my_str, n):
    answer = []
    st, ed = 0, n
    while st < len(my_str):
        answer.append(my_str[st : min(ed, len(my_str))])
        st += n
        ed += n
    return answer