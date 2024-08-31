def solution(storey):
    answer = 0
    loop = len(str(storey))
    div = 10
    one = storey % div
    two = (storey-one) % (div * 10)
    
    if one == 5 and two >= 50:
        storey += div - one
        answer += (div-one) // (div // 10)
    elif one == 5 and two < 50:
        storey -= one
        answer += one // (div // 10)
    while storey != 0:
        mod = storey % div
        if mod > 5 * div//10:
            storey += div - mod
            answer += (div-mod) // (div // 10)
        else:
            storey -= mod
            answer += mod // (div // 10)
        div *= 10
        loop -= 1
    return answer