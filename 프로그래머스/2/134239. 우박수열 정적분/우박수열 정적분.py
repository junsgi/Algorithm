def collatz(k):
    res = [k]
    while k != 1:
        if k % 2:
            k = k * 3 + 1
        else:
            k //= 2
        res.append(k)
    return res
def CCW(x1, y1, x2, y2, x3, y3):
    return ((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)) / 2
    
def solution(k, ranges):
    answer = []
    arr = collatz(k)
    LEN = len(arr) - 1
    for a, b in ranges:
        END = LEN - (-b)
        if a > END: answer.append(-1.0)
        elif a == END: answer.append(0.0)
        else:
            S = 0
            for i in range(a + 1, END + 1):
                S += CCW(a, 0, i - 1, arr[i - 1], i, arr[i])
            answer.append(abs(S + CCW(a, 0, END, arr[END], END, 0)))
    return answer