def is_prime(number):
    if number < 2:
        return False 

    for i in range(3, int(number**0.5) + 1):
        if number % i == 0:
            return False  

    return True

a = int(input())
idx = 3
while a != 1:
    if a % 2 == 0:
        print(2)
        a //= 2 
    elif a % 2 != 0 and a % idx == 0 and is_prime(idx):
        print(idx)
        a //= idx 
        idx = 3
    else:
        idx += 1