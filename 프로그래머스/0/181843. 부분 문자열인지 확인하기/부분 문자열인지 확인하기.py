M, K = 100_003, 31
def solution(my_string, target):
    global M, K
    N = len(target)
    t = 0
    for i in target:
        c = ord(i)
        t = (t + c * K) % M
    target = t
    t = 0
    for i in range(len(my_string)):
        c = ord(my_string[i])
        if i < N:
            t = (t + c * K) % M
        else: # 해시를 이용한 슬라이딩 윈도우
            d = ord(my_string[i - N])
            t = (t - d * K) % M
            t = (t + c * K) % M
        if t == target:
            return 1
    return 0
