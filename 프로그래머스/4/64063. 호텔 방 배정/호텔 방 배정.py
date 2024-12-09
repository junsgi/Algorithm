import sys
sys.setrecursionlimit(200003)
def solution(k, room_number):
    answer = []
    check = {}
    def find(node):
        if node not in check:
            check[node] = node + 1
            return node
        check[node] = find(check[node])
        return check[node]
    for i in room_number:
        answer.append(find(i))
    return answer