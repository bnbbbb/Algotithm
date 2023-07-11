def solution(numbers, hand):
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    le = '*'
    ri = '#'
    answer = ''
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            le = num
        elif num in [3, 6, 9]:
            answer += 'R'
            ri = num
        else:
            left = abs(keypad[le][0] - keypad[num][0]) + abs(keypad[le][1]-keypad[num][1])
            right = abs(keypad[ri][0] - keypad[num][0]) + abs(keypad[ri][1]-keypad[num][1])
            if left < right:
                answer += 'L'
                le = num
            elif left > right:
                answer += 'R'
                ri = num
            else:
                if hand == 'left':
                    answer += 'L'
                    le = num
                else:
                    answer += 'R'
                    ri = num
    return answer