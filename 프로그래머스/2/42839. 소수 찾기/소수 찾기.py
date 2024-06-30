nums = set()
def p(depth, check, num, value):
    if depth == len(num):
        return
    for i in range(len(num)):
        if check & (1 << i): continue
        if int(value + num[i]) >= 2:
            nums.add(int(value + num[i]))
        n = p(depth + 1, check | (1 << i), num, value + num[i])
def solution(numbers):
    global nums
    answer = 0
    p(0, 0, numbers, "")
    for i in nums:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            answer += 1
    return answer