import math

def solution(arrayA, arrayB):
    answer = 0
    gcd_A = arrayA[0]
    gcd_B = arrayB[0]

    for num in arrayA[1:]:
        gcd_A = math.gcd(gcd_A, num)

    for num in arrayB[1:]:
        gcd_B = math.gcd(gcd_B, num)

    gcd_A, gcd_B
    if all(num2 % gcd_A != 0 for num2 in arrayB):
        if answer < gcd_A:
            answer = gcd_A
    if all(num % gcd_B != 0 for num in arrayA):
        if answer < gcd_B:
            answer = gcd_B
    
    return answer