def is_prime(number):
    if number < 2:
        return False 

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  

    return True

a = int(input())
answer = 0
li = list(map(int, input().split()))

for i in li:
    if is_prime(i):
        answer += 1
print(answer)
