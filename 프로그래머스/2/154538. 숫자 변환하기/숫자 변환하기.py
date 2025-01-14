from collections import deque
def solution(x, y, n):
    answer = 0
    que = deque()
    que.append(x)
    c = [0] * (y + 1)
    c[x] = 1
    while que:
        a = que.popleft()
        if a == y: break
        if a + n <= y and c[a + n] == 0:
            c[a + n] = c[a] + 1
            que.append(a + n)
        
        if a * 2 <= y and c[a * 2] == 0:
            c[a * 2] = c[a] + 1
            que.append(a * 2)
        
        if a * 3 <= y and c[a * 3] == 0:
            c[a * 3] = c[a] + 1
            que.append(a * 3)
            
    return c[y] - 1