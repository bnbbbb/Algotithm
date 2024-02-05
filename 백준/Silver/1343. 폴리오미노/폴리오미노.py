def solve(poli, n):
    result = ['.'] * n
    i = 0
    if poli == 'X':
        return -1
    while i < n:
        if poli[i] == 'X' and i + 4 <= n and '.'not in poli[i:i+4]:
            result[i:i+4] = 'AAAA'
            i += 4
        elif i + 2 <= n and poli[i:i+2] == 'XX':
            result[i:i+2] = 'BB'
            i += 2
        elif i + 1 < n and poli[i] == 'X' and poli[i+1] !='X':
            result = []
            break
        elif poli[i]!= 'X':
            result[i] = '.'
            i += 1
        else:
            result = []
            break
    return ''.join(result) if result else -1

poli = input()
print(solve(poli, len(poli)))
