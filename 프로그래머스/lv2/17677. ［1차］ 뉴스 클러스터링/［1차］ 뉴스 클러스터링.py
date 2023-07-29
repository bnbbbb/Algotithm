from collections import Counter
def solution(str1, str2):
    answer = 0
    ans1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    ans2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    ans1 = Counter(ans1)
    ans2 = Counter(ans2)
    
    a = ans1 & ans2
    b = ans1 | ans2
    
    total1 = sum([value for _, value in a.items()])
    total2 = sum([value for _, value in b.items()])
    
    if total1 == total2:
        return 65536
    answer = total1 / total2
    return answer * 65536 // 1