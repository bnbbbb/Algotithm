from itertools import combinations
def solution(nums):
    answer = 0
    result = [sum(i) for i in list(combinations(nums, 3))]
    for i in result:
        prime = 0
        for j in range(2, i+1):
            if i % j == 0:
                prime += 1
        if prime == 1:
            answer += 1
    return answer