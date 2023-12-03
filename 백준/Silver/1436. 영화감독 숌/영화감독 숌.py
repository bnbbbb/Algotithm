def check_number(n):
    count = 0
    number = 666
    while True:
        if '666' in str(number):
            count +=1
        if count ==n:
            return number
        number += 1
n = int(input())
result = check_number(n)
print(result)
