def is_prime(number):
    if number < 2:
        return False 

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  

    return True

a = int(input())
b = int(input())
li = [i for i in range(a, b+1) if is_prime(i)]


if li:
    print(sum(li))
    print(min(li))
else:
    print(-1)