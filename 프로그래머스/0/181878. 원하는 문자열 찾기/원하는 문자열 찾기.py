def solution(myString, pat):
    return 1 if pat.lower() in myString.lower() else 0
    M, K = 391, 31
    a, b = myString.lower(), pat.lower()
    t = 0
    for i in b:
        k = ord(i)
        t = (t + k * K) % M
        
    key = 0
    for i in range(len(a)):
        k = ord(a[i])
        if i < len(b):
            key = (key + k * K) % M
        else: 
            prev = ord(a[i - len(b)])
            key = (key - prev * K) % M
            key = (key + k * K) % M
        if key == t:
            return 1
    return 0
