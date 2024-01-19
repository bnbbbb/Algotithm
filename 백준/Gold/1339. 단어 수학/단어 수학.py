n = int(input())
words = [input().strip() for _ in range(n)]

alpha_values = {}
for word in words:
    for i, char in enumerate(word[::-1]):
        if char not in alpha_values:
            alpha_values[char] = 0
        alpha_values[char] += 10 ** i
sorted_alpha_values = sorted(alpha_values.items(), key=lambda x: x[1], reverse=True)

assigned_values = {}
current_value = 9
for char, value in sorted_alpha_values:
    assigned_values[char] = current_value
    current_value -= 1

total_sum = 0
for word in words:
    number = int(''.join(str(assigned_values[char]) for char in word))
    total_sum += number

print(total_sum)