def solution(sequence, k):
    answer = []
    min_len = float('inf')
    total = 0
    start = 0

    for end in range(len(sequence)):
        total += sequence[end]
        while total > k:
            total -= sequence[start]
            start += 1 
        if total == k:
            if end - start < min_len:
                min_len = end - start
                answer = [start, end]

    return answer if answer else []