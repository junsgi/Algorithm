# https://www.acmicpc.net/problem/3447
import sys
import re
for i in sys.stdin:
    syn = i.strip()
    if not syn:
        print()
        continue
    check = re.search("(BUG)+", syn)
    while syn and check:
        x, y = check.span()
        syn = syn[:x] + syn[y:]
        check = re.search("(BUG)+", syn)
    print(syn)