# https://www.acmicpc.net/problem/5637
import re
ans = ''
while 1:
    syn = input().split()
    for w in syn:
        if not re.search("^[a-zA-Z\-]+$", w): continue
        if len(ans) < len(w):
            ans = w
        if w == 'E-N-D':
            print(ans.lower())
            exit()
        