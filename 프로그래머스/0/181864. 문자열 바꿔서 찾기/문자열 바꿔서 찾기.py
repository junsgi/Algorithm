def solution(myString, pat):
    a = ""
    for i in myString:
        if i == "A": a += "B"
        else : a += "A"
    return 1 if pat in a else 0