def solution(myString, pat):
    count = 0
    while 1: 
        x = myString.find(pat)
        myString = myString[x+1:]
        if x == -1:
            break
        count +=1
    return count