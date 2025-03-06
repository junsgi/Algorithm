옹알이 = ["aya", "ye", "woo", "ma"]
def 함수(깊이, 탈출, 검사, 결과):
    if 깊이 == 탈출 or len(결과) >= 30:
        return [결과]
    임시 = []
    for 인덱스 in range(4):
        if 검사 == 인덱스: continue
        임시.extend(함수(깊이 + 1, 탈출, 인덱스, 결과 + 옹알이[인덱스]))
    return 임시
def solution(babbling):
    정답 = 0
    배열 = babbling
    조합 = []
    for 깊이 in range(1, 11):
        조합.extend(함수(0, 깊이, -1, ""))
    for 옹알 in 배열:
        if 옹알 in 조합:
            정답 += 1
    return 정답