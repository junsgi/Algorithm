# https://www.acmicpc.net/problem/12904
s = input()
t = input()
def req(s, t):
    if s == t:
        return 1
    if len(s) == len(t):
        return 0
    if t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
        return req(s, t)
    else:
        return req(s, t[:-1])
print(req(s, t))