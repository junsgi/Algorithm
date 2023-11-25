# https://school.programmers.co.kr/learn/courses/30/lessons/72412
def solution(info, query):
    answer = []
    dic = {}
    for i in range(len(info)):
        print(info[i].split(' '))
        for w in info[i].split(' '):
            if w in dic:
                dic[w] += 1
            else:
                dic[w] = 1
    print(dic)
    for q in query:
        words = q.split(" ")
        print(words)
        cnt = 0x7fffffff
        
        for i in range(0, len(words), 2):
            if words[i] == '-':
                cnt = min(cnt, len(query))
            elif words[i] in dic:
                cnt = min(cnt, dic[words[i]])
        answer.append(cnt)
            
    return answer

print(solution(
    ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
    ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
))