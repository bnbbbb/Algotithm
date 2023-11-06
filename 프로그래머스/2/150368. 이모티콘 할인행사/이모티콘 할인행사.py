from itertools import product
def solution(users, emoticons):
    result = []
    rate = [10, 20, 30, 40]
    discount_cases = list(product(rate, repeat=len(emoticons)))
    for case in discount_cases:
        max_total = 0
        plus = 0
        for req, budget in users:
            purchased = 0
            for i in range(len(emoticons)):
                if req <= case[i]:
                    purchased += emoticons[i] - emoticons[i] * case[i] *0.01
            if purchased >= budget:
                plus += 1
            else:
                max_total += purchased
        result.append((plus, max_total))
    answer = sorted(result, key = lambda x: (x[0], x[1]), reverse=True)
    
    return answer[0]