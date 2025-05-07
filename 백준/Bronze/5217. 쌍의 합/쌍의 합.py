T = int(input())
for _ in range(T):
    num = int(input())
    if num == 2: print('Pairs for 2:')
    else:
        one = 1
        result = []
        while num:
            if num-one < one or num-one == one:break
            result.append(f'{one} {abs(num-one)}')
            one += 1
        print(f"Pairs for {num}: {', '.join(result)}")