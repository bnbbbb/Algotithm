def solution(phone_book):
    result = sorted(phone_book)
    for i in range(len(result)-1):
        if result[i] == result[i+1][:len(result[i])]:
            return False
        
    return True