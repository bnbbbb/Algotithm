def find_rank(N, people):
    ranks = [1] * N  # 초기 등수를 1로 초기화

    for i in range(N):
        for j in range(N):
            if i != j:
                # i번째 사람과 j번째 사람을 비교하여 덩치 등수 증가
                if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                    ranks[i] += 1

    return ranks

# 입력 받기
N = int(input())
people = []
for _ in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))

# 덩치 등수 계산
result = find_rank(N, people)

# 결과 출력
print(" ".join(map(str, result)))