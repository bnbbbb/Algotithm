from collections import Counter

def make_palindrome(name):
    char_count = Counter(name)
    odd_count = sum(count % 2 for count in char_count.values())
    if odd_count > 1:
        return "I'm Sorry Hansoo"

    half_palindrome = []
    middle_char = ""

    for char, count in char_count.items():
        half_count = count // 2
        half_palindrome.extend([char] * half_count)
        if count % 2 == 1:
            middle_char = char

    half_palindrome.sort()

    result = ''.join(half_palindrome) + middle_char + ''.join(reversed(half_palindrome))
    return result

name = input().strip()

result = make_palindrome(name)

print(result)