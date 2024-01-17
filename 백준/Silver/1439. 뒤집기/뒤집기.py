def min_flip_count(s):
    count_0 = 0  # 연속된 0의 그룹 수
    count_1 = 0  # 연속된 1의 그룹 수

    # 문자열의 첫 번째 문자에 대한 초기화
    if s[0] == '0':
        count_0 += 1
    else:
        count_1 += 1

    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            if s[i] == '0':
                count_0 += 1
            else:
                count_1 += 1

    return min(count_0, count_1)

# 입력 받기
S = input()

# 결과 출력
print(min_flip_count(S))
