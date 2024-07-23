n = int(input())
temp = 1
answer = 3
while (n := n - 1) != 0:
    answer, temp = (answer * 2 + temp) % 9901, answer
print(answer)