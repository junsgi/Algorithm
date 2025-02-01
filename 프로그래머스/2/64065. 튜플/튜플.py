def solution(s):
    answer = []
    s = s.replace("{", "(")
    s = s.replace("}", ", )")
    s = eval(s)
    arr = []
    for i in s:
        arr.append(list(i))
    arr.sort(key = lambda x : len(x))
    
    c = set()
    for i in arr:
        for j in i:
            if j in c: continue
            answer.append(j)
            c.add(j)
    return answer