import sys
input = sys.stdin.readline
n = int(input().strip())
p = [] # 양수배열
m = [] # 음수배열
z = False
for _ in range(n):
    num = int(input().strip())
    if num > 0:
        p.append(num)
    elif num < 0:
        m.append(num)
    else:
        z = True

p.sort(reverse=True)
t1 = 0
for i in range(1, len(p), 2):
    # 1 * 1의 경우 2가 더 크므로 max함수 사용
    t1 += max(p[i] * p[i-1], p[i] + p[i-1])

# 양수 배열의 길이가 홀수라면 마지막 요소를 더합니다.
if len(p) % 2:
    t1 += p[len(p) - 1]

t2 = 0

if len(m) == 1:
    # 입력에 0이 있었다면 0을 곱하여 더합니다.
    if z:
        print(t1)

    # 0이 없었다면 음수 하나를 더합니다
    else:
        print(t1 + m[0])
else:

    m.sort()
    for i in range(1, len(m), 2):
        t2 += m[i] * m[i-1]
    
    if len(m) % 2:
        # 음수 배열의 길이가 홀수이면서 0이 존재했다면 0을 곱해버립니다.
        if z:
            print(t1 + t2)
        else:
            print(t1 + t2 + m[len(m) - 1])
    else:
        print(t1 + t2)
