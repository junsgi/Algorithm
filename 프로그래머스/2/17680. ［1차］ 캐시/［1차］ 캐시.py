def solution(cacheSize, cities):
    if cacheSize == 0: return 5 * len(cities)
    answer = 0
    for i in range(len(cities)): cities[i] = cities[i].lower()
    cache = {}
    head = ""
    tail = ""
    for i in cities:
        if not cache or i not in cache: # miss
            answer += 5
            if len(cache) == cacheSize:
                if cache[head][1]:
                    t = cache[head][1]
                    cache[cache[head][1]][0] = ""
                    del cache[head]
                    head = t
                else:
                    cache.clear()
                    head = ""
                    tail = ""
            if not head:
                head = i
                tail = i
                cache[head] = ["", ""]
            else:
                cache[tail][1] = i
                cache[i] = [tail, ""]
                tail = i
        else:
            answer += 1
            if cache[i][0]:
                cache[cache[i][0]][1] = cache[i][1]
            elif cache[i][1]:
                head = cache[i][1]
                
            if cache[i][1]:
                cache[cache[i][1]][0] = cache[i][0]
            elif cache[i][0]:
                tail = cache[i][0]
            cache[tail][1] = i
            cache[i][0] = tail
            cache[i][1] = ""
            tail = i
    return answer