def solution(myString, pat):
    
    x = myString.rfind(pat)
    answer= myString[:x+len(pat)]
    
    return answer