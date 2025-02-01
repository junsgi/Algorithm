def solution(storey):
    answer = 0
    if storey <= 5: return storey
    while storey:
        if storey <= 5 or storey % 10 < 5 or (storey % 10 == 5 and storey // 10 % 10 < 5):
            answer += storey % 10
        else:
            answer += 10 - storey % 10
            storey += 10
        storey //= 10
    
    return answer