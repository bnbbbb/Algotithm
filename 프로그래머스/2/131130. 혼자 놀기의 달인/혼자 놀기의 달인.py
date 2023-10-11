def solution(cards):
    result = []
    idx = 0
    count = 0
    while cards.count('x') != len(cards):
        answer = 0
        while idx != len(cards):
            if cards[idx] != 'x':
                cards[idx], idx = 'x', cards[idx]-1
                answer += 1
            elif cards[idx] == 'x':
                for i in range(len(cards)):
                    if cards[i] != 'x':
                        idx = i
                break
        result.append(answer)
        count += 1
        
    result.sort(reverse=True)
    return result[0] * result[1] if len(result) > 1 else 0