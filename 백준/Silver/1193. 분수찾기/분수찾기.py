def find_fraction(x):
    n = 1
    while x > n:
        x -= n
        n += 1
    if n % 2 == 0:
        numerator = x
        denominator = n - x + 1
    else:
        numerator = n - x + 1
        denominator = x
    return f"{numerator}/{denominator}"

x = int(input())

result = find_fraction(x)
print(result)