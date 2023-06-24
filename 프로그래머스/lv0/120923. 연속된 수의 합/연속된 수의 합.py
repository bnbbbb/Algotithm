def solution(num, total):
    answer = []
    i = -num
    a = list(range(-num, num+total)) 
    b = len(a) + 1
    
    for i in range(b):
        for j in range(b):
            if sum(a[i:j]) == total and len(a[i:j]) == num:
                answer.extend(a[i:j])
    return answer
