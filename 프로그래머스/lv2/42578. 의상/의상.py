def solution(clothes):
    clothes_count = {}
    for _, category in clothes:
        if category in clothes_count:
            clothes_count[category] += 1
        else:
            clothes_count[category] = 1
    
    answer = 1
    for count in clothes_count.values():
        answer *= (count + 1)  
    
    return answer - 1  