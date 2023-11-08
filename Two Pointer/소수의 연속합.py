# https://www.acmicpc.net/problem/1644

n = int(input())
if not n:
    print(n)
    exit()
prime = [0 if i % 2 else 1 for i in range(n + 1)]
prime[1] = 1
if n > 1:
    prime[2] = 0

arr = [0, 2]
def isPrime(x):
    global n
    for i in range(2, x):
        if not i * i <= x:
            return True
        if x % i == 0: 
            return False
    for i in range(x + x, n + 1, x):
        prime[i] = 1
    return True

stop = False
for i in range(3, n + 1, 2):
    result = False
    if prime[i] == 0:
        result = isPrime(i)
    if result:
        if i > n: break
        arr.append(i + arr[-1])
p1 = 0
p2 = 1
answer = 0
while p2 < len(arr) and p1 != p2:
    mid = arr[p2] - arr[p1]
    if mid == n: 
        answer += 1
    if mid <= n:
        p2 += 1
    elif n < mid:
        p1 += 1
print(answer)

"""
7 2
7 3
7 4
7 5
7 6

"""