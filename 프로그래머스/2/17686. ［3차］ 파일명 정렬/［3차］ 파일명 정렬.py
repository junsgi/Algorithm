def solution(files):
    answer = []
    a=[]
    for x in range(len(files)):
        i = files[x]
        idx = 0
        head, num = "", ""
        while 1:
            if i[idx].isdigit(): break
            head+=i[idx]
            idx+=1
        while 1:
            if idx==len(i) or not i[idx].isdigit():
                break
            num+=i[idx]
            idx+=1
        a.append((head.lower(), int(num), x, i))
    a.sort()
    for _, _, _, ans in a:
        answer.append(ans)
    return answer