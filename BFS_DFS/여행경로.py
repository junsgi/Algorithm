# https://school.programmers.co.kr/learn/courses/30/lessons/43164
def solution(tickets):
    answer = []
    check = [0] * len(tickets)
    def DFS(airport, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return
        for i in range(len(tickets)):
            if airport == tickets[i][0] and check[i] == 0:
                check[i] = 1
                DFS(tickets[i][1], path + [tickets[i][1]])
                check[i] = 0
    DFS('ICN', ['ICN'])
    # 길이는 전부 같기 때문에 알파벳 순으로 정렬됩니다.
    return sorted(answer)[0]