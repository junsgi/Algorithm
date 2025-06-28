T = int(input())
for i in range(T):
    m = list(input().split())
    sum = 0.0
    for j in m:
        if type(j) == str and j == '%':
            sum = sum + 5

        elif type(j) == str and j == '@':
            sum = sum * 3

        elif type(j) == str and j == '#':
            sum = sum - 7

        elif type(float(j)) == float:
            sum += float(j)
    print('%.2f'%sum)