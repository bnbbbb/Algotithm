def base_b_to_base_10(n, b):
    result = 0
    for i, digit in enumerate(reversed(str(n))):
        if '0' <= digit <= '9':
            result += int(digit) * (b ** i)
        else:
            result += (ord(digit) - ord('A') + 10) * (b ** i)
    return result

n, b = map(str, input().split())

result = base_b_to_base_10(n, int(b))

print(result)