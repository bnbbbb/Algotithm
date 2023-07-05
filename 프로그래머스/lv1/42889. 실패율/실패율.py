from collections import Counter

def solution(N, stages):
    counter = Counter(stages)
    total = len(stages)
    failure_rates = []

    for stage in range(1, N+1):
        failure_rate = counter[stage] / total if total > 0 else 0
        failure_rates.append((stage, failure_rate))
        total -= counter[stage]

    failure_rates.sort(key=lambda x: x[1], reverse=True)
    answer = [stage for stage, _ in failure_rates]
    return answer