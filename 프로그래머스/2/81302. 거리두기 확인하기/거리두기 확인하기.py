def solution(places):
    answer = []
    for table in places:
        P = []
        X = []
        for i in range(5):
            for j in range(5):
                if table[i][j] == 'P':
                    P.append((i, j))

                if table[i][j] == 'X':
                    X.append((i, j))
        for i in range(len(P)):
            flag = False
            for j in range(i + 1, len(P)):
                dist = abs(P[i][0] - P[j][0]) + abs(P[i][1] - P[j][1])
                if dist <= 2:
                    cnt = 0
                    for k in range(len(X)):
                        if min(P[i][0], P[j][0]) <= X[k][0] <= max(P[i][0], P[j][0]) and \
                           min(P[i][1], P[j][1]) <= X[k][1] <= max(P[i][1], P[j][1]):
                                cnt += 1
                    if not cnt or (P[i][0] != P[j][0] and P[i][1] != P[j][1] and cnt != 2):
                        answer.append(0)
                        flag = True
                        break
            if flag:
                break
        else:
            answer.append(1)
                        
    return answer