def solution(phone_book):
    phone_book.sort(key = lambda x : len(x))
    HashSet = set()
    HashSet.add(phone_book[0])
    st = len(phone_book[0])
    ed = st
    for i in range(1, len(phone_book)):
        for j in range(st, ed + 1):
            if phone_book[i][:j] in HashSet:
                return False
        ed = len(phone_book[i])
        HashSet.add(phone_book[i])
    return True