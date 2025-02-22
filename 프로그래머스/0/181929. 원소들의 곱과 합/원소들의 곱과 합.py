def solution(num_list):
    answer = 0
    n1 = 1
    for i in num_list:
        n1 *= i
    return 1 if n1 < sum(num_list)**2 else 0