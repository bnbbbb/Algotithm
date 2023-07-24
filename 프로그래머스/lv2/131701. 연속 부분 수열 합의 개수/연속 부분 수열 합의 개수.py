def solution(elements):
    answer = []
    n = len(elements)
    linear = elements + elements
    sub_sums = set()
    for i in range(n):
        for j in range(i, i + n):
            sub_sum = sum(linear[i:j+1])
            sub_sums.add(sub_sum)
    answer = len(sub_sums)
    return answer