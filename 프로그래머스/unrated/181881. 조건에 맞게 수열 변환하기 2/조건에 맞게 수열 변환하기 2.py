def solution(arr):
    answer = []
    count = 0
    while True:
        answer = [(i // 2) if i >= 50 and i % 2 == 0 else (i * 2)+1 if i < 50 and i % 2 != 0 else i for i in arr]
        
        if answer == arr:
            break
        arr = answer
        count +=1
        
    return count