import re
def solution(word, pages):
    word = word.lower()
    info = []
    graph = {}
    for i in range(len(pages)):
        name = re.search('<meta property=\"og:url\" content=\"https://([\S]+)\".*/>', pages[i]).group(1) #현재 url검색
        
        link = re.findall('<a href=\"https://(\S+)\">', pages[i]) #외부 링크 url 전부 검색
        
        score = 0
        for j in re.findall("[a-zA-Z]+", pages[i].lower()):
            if j == word:
                score += 1
        data = {
            "name" : name,
            "index" : i,
            "score" : score,
            "to" : link,
            "link" : 0
        }
        graph[name] = data
        info.append(data)
    for i in info:
        for j in i["to"]:
            if j in graph.keys():
                graph[j]["link"] += graph[i["name"]]["score"] / len(graph[i["name"]]["to"])
    answer = 0
    m = 0
    for i in graph.keys():
        if m < graph[i]["score"] + graph[i]["link"]:
            m = graph[i]["score"] + graph[i]["link"]
            answer = graph[i]['index']
    return answer