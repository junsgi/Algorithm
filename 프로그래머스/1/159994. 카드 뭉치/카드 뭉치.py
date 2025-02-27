def solution(cards1, cards2, goal):
    c1 = 0
    c2 = 0
    g = 0
    while g < len(goal) and c1 < len(cards1) and c2 < len(cards2):
        if cards1[c1] == goal[g]:
            c1 += 1
        elif cards2[c2] == goal[g]:
            c2 += 1
        else:
            return "No"
        g += 1
    while g < len(goal) and c1 < len(cards1):
        if cards1[c1] == goal[g]:
            c1 += 1
        else:
            return "No"
        g += 1
    
    while g < len(goal) and c2 < len(cards2):
        if cards2[c2] == goal[g]:
            c2 += 1
        else:
            return "No"
        g += 1
    return "Yes"