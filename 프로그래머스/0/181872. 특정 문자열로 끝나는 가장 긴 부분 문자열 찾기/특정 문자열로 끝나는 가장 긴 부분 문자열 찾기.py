def solution(myString, pat):
    myString = myString[::-1]
    pat = pat[::-1]
    a = myString.find(pat)
    if a == -1 : return myString[::-1]
    else: return myString[a:][::-1]
