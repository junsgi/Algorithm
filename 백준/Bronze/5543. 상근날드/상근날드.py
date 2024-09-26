result = []
for _ in range(5):
    result.append(int(input()))
juice = []
juice.append(result.pop())
juice.append(result.pop())
print(min(result)+min(juice)-50)