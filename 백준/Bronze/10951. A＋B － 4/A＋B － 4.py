import sys
while True:
    try:
        num1, num2 = map(int, sys.stdin.readline().split())
        print(f'{num1 + num2}')
    except KeyboardInterrupt:
        break
    except ValueError:
        break