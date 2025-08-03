num1, num2 = map(int,input().split())

if num1 > num2:
    max = num1
    min = num2
else:
    max = num2
    min = num1

if max - min == 0:
    print(max-min)
else:
    print((max-min)-1)
while min < max:
    min += 1
    if min == max:break
    print(min,end=' ')