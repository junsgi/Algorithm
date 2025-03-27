def solution(brown, yellow):

    카펫크기 = brown + yellow # 카펫 전체 크기
    약수 = []

    # 약수들로만 계산하기 위해 약수 구함
    for i in range(3, 카펫크기 // 3 + 1): 
        if 카펫크기 % i == 0:
            약수.append(i)
    print(약수)
    for i in range(len(약수)):
        세로 = 약수[i]
        가로 = 카펫크기 // 세로
        if (가로 - 2) * (세로 - 2) == yellow:
            return [가로, 세로]