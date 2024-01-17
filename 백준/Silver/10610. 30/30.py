def convert_thirty(n):
    if '0' not in n:
        return -1

    digit_count = [0] * 10
    total = 0

    for digit in n:
        digit = int(digit)
        digit_count[digit] += 1
        total += digit

    if total % 3 != 0:
        return -1

    result = ''
    for i in range(9, -1, -1):
        result += str(i) * digit_count[i]

    return int(result)

n = input()
print(convert_thirty(n))