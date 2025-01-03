def hanoi(n, before, after):
    if n == 0:
        return
    hanoi(n - 1, before, 6 - (after + before))
    print(before, after)
    hanoi(n - 1, 6 - (after + before), after)
n = int(input())
print(2 ** n - 1)
if n <= 20:
    hanoi(n, 1, 3)