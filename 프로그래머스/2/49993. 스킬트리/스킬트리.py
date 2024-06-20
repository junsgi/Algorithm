def solution(skill, skill_trees):
    answer = 0
    check = {}
    for i in range(len(skill)): check[skill[i]] = str(i)
    res = "".join([f"{i}" for i in range(len(skill))])
    for sk in skill_trees:
        temp = ""
        for i in range(len(sk)):
            if sk[i] in check:
                temp += check[sk[i]]
        if temp == res[:len(temp)]:
            answer += 1
    return answer