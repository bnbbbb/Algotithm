def solution(brown, yellow):
    alc = brown + yellow
    
    result = []
    for i in range(1, int(alc**(1/2))+1):
        if alc%i==0:
            result.append(i)
            if i < alc//i:
                result.append(alc//i)
    high = sorted(result, reverse=True)
    low = sorted(result)
    for x, y in zip(high, low):
        if x >= y and (x-2) * (y-2) == yellow:
            return [x, y]