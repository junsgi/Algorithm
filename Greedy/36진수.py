# https://www.acmicpc.net/problem/1036
alpha = { chr(x) : int(chr(x), 36) for x in range(65, 91) }
for i in range(10): alpha[str(i)] = i
check = [[0] * 51 for i in range(37)]
n = int(input())
words = [input() for _ in range(n)]
k = int(input())

for w in words:
    zero = len(w) - 1
    for i in w:
        check[alpha[i]][zero] += 1
        zero -= 1


def Sum(n, m):
    bit = 0
    n, m = sorted((n, m), key = lambda x : len(x))
    n = "0" * (len(m) - len(n)) + n
    idx = len(n) - 1
    result = ""
    
    while idx >= 0:
        tn = int(n[idx])
        tm = int(m[idx])
        s = tn + tm
        if s > 9:
            if not bit:
                result += str(s % 10)
            else:
                result += str(s % 10 + 1)
            bit = 1
        else:
            if not bit:
                result += str(s)
            else:
                if s + 1 > 9:
                    result += str((s + 1) % 10)
                    bit = 1
                else:
                    result += str(s + 1)
                    bit = 0
        idx -= 1
    return result[::-1] if not bit else "1" + result[::-1]