from string import ascii_uppercase
def solution(msg):
    answer = []
    alp = dict(zip(ascii_uppercase, range(1, len(ascii_uppercase)+1)))
    w = msg[0]
    for i in msg[1:]:
        max_key = alp.get(max(alp.keys(), key = lambda x: alp[x]))
        word = w + i
        if word in alp:
            w = word
        else:
            answer.append(alp[w])
            alp[word] = max_key + 1
            w = i
    answer.append(alp[w])
    return answer