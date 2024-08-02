n = int(input())
arr = tuple(map(int, input().split()))
acs, acsLEN, desc, descLEN = 1, 1, 1, 1
for i in range(1, n):
    if arr[i - 1] <= arr[i]:
        acsLEN += 1
    else:
        acs = max(acs, acsLEN)
        acsLEN = 1
    
    if arr[i - 1] >= arr[i]:
        descLEN += 1
    else:
        desc = max(desc, descLEN)
        descLEN = 1
acs = max(acs, acsLEN)
desc = max(desc, descLEN)
print(max(desc, acs))