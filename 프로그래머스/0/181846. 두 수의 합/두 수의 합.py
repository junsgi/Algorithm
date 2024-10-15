def solution(a, b):
    answer = ''
    one = 0
    if len(a) > len(b):
        a, b = b, a
    ai, bi = len(a) - 1, len(b) - 1
    for _ in range(len(a)):
        an, bn = int(a[ai]), int(b[bi])
        answer += str((an + bn + one) % 10)
        if an + bn + one >= 10:
            one = 1
        else:
            one = 0
        ai -= 1
        bi -= 1
    while bi >= 0:
        bn = int(b[bi])
        answer += str((bn + one) % 10)
        if bn + one >= 10: one = 1
        else: one = 0
        bi -= 1
    if one:
        answer += '1'
    return answer[::-1]