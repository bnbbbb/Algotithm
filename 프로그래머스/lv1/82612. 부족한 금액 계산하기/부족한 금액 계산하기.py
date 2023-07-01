def solution(price, money, count):
    answer = 0
    while count != 0:
        answer += price*count
        count -= 1
    result = money - answer
    
    return abs(result) if money < answer else 0