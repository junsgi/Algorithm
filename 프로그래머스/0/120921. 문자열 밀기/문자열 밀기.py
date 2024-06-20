def solution(A, B):
    answer = 0
    idx = 0
    search = 0
    cnt = 0
    LEN = len(A)
    c = -1
    while cnt != LEN:
        if A[idx] == B[search % LEN]:
            cnt += 1
            idx += 1
            if c == -1 : c = search % LEN
        else:
            c = -1
            cnt = 0
            idx = 0
            if A[idx] == B[search % LEN]:
                cnt = 1
                idx = 1
                c = search % LEN
        search += 1
        if search >= LEN * 10: return -1
    return c