# https://www.acmicpc.net/problem/2251
A, B, C = map(int, input().split())
check = set()
ans = []
def DFS(a, b, c):
    global A, B, C
    if f'{a}{b}{c}' in check: return
    if not a:
        ans.append(c)
    check.add(f'{a}{b}{c}')
    if a > B - b: # A -> B
        DFS(a - (B - b), B, c)
    else:
        DFS(0, a + b, c)

    if a > C - c: # A -> C
        DFS(a - (C - c), b, C)
    else:
        DFS(0, b, a + c)

    if b > A - a: # B -> A
        DFS(A, b - (A - a), c)
    else:
        DFS(a + b, 0, c)
    
    if b > C - c: # B -> C
        DFS(a, b - (C - c), C)
    else:
        DFS(a, 0, b + c)
    
    if c > A - a: # C -> A
        DFS(A, b, c - (A - a))
    else:
        DFS(a + c, b, 0)
    
    if c > B - b: # C -> B
        DFS(a, B, c - (B - b))
    else:
        DFS(a, b + c, 0)
DFS(0, 0, C)
print(*sorted(ans))