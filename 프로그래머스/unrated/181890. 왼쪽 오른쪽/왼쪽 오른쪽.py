def solution(text):
    answer = []
    try:
        if 'l' in text and 'r' not in text:
            for i in range(text.index('l')):
                answer.append(text[i])
        elif 'r' in text and 'l' not in text:
            for i in range(text.index('r')+1, len(text)):
                answer.append(text[i])
        elif text.index('l') < text.index('r') :
            for i in range(text.index('l')):
                answer.append(text[i])
        elif text.index('l') > text.index('r'):
            for i in range(text.index('r')+1, len(text)):
                answer.append(text[i])
    except ValueError:
        return answer
    return answer