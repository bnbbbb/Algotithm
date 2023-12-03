def calculate_sum_of_digits(number):
    return sum(map(int, str(number)))

def find_constructor(N):
    for candidate in range(1, N + 1):
        if candidate + calculate_sum_of_digits(candidate) == N:
            return candidate
    return 0

# 입력 받기
N = int(input())

# 결과 출력
result = find_constructor(N)
print(result)