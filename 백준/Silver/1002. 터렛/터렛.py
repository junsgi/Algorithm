import math as m
N = int(input())

for _ in range(N):
    x1, y1, ar, x2, y2, br = map(int, input().split())

    if x1 == x2 and y1 == y2:
        if ar == br:
            print(-1)
        else:
            print(0)

    else:
        space = m.sqrt((x1-x2)**2+(y1-y2)**2)
        
        if space == ar + br:
            print(1)

        elif space > ar + br:
            print(0)
        

        else:
            max = ar
            min = br
            if ar < br: max, min = br, ar

            if space == max - min:
                print(1)
            elif space < max - min:
                print(0)


            else: print(2)
