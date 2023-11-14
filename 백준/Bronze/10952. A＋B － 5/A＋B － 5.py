import sys
while True:
    num1, num2 = map(int, sys.stdin.readline().split())
    if num1 == 0 and num2 == 0:
        break    
    print(f'{num1 + num2}')