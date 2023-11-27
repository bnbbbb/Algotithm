def base_10_to_base_b(n,b):
    result = ""
    while n > 0:
        remainder = n % b
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result
        n //= b
    return result if result else "0"

n, b = map(int, input().split())

result = base_10_to_base_b(n, b)

print(result)