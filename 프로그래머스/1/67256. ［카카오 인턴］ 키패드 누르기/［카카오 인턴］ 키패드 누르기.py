def solution(numbers, hand):
    answer = ''
    loc = [(3, 1)]
    for i in range(9):
        loc.append((i // 3, i % 3))
    left = (3, 0)
    right = (3, 2)
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            left = loc[n]
            answer += "L"
        elif n == 3 or n == 6 or n == 9:
            right = loc[n]
            answer += "R"
        else:
            ld = abs(loc[n][0] - left[0]) + abs(loc[n][1] - left[1])
            rd = abs(loc[n][0] - right[0]) + abs(loc[n][1] - right[1])
            if ld == rd:
                if hand == 'left':
                    answer += "L"
                    left = loc[n]
                else:
                    answer += "R"
                    right = loc[n]
            elif ld < rd:
                answer += "L"
                left = loc[n]
            else:
                answer += "R"
                right = loc[n]
        
    return answer