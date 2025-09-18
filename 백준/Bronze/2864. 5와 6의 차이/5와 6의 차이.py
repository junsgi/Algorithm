n, m = input().split()
MAX = int(n.replace("5", "6")) + int(m.replace("5", "6"))
MIN = int(n.replace("6", "5")) + int(m.replace("6", "5"))
print(MIN, MAX)