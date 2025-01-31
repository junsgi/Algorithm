def isPrime(n):
    if n == 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def solution(n, k):
    answer = 0
    res = ""
    while n:
        res += str(n % k)
        n //= k
    for i in map(lambda x : 4 if not x else int(x), res[::-1].strip("0").split("0")):
        if isPrime(i):
            answer += 1
    
    return answer