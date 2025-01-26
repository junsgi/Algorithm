def solution(myString):
    arr = []
    t = ""
    for i in myString:
        if i == "x" and t:
            arr.append(t)
            t = ""
        elif i != "x":
            t += i
    if t: arr.append(t)
    arr.sort()
    return arr
