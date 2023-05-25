def solution(a):
    answer = 0
    a = a.split()
    c = []
    d = []
    x = 0
    n = 0
    for i in a:
        if 'x' in i and len(i) > 1:
            b = i.replace('x', '+x')
            c.append(b.split('+'))
        elif 'x' in i and len(i) == 1:
            b = i.replace('x', '1+x')
            c.append(b.split('+'))
        elif 'x' not in i and i.isdigit():
            d.append(int(i))
            n = sum(d)
    for i in range(len(c)):
        x += int(c[i][0])
    if n == 0 and x != 0:
        answer = str(x)+'x'
        answer = answer.replace('1x', 'x')
    elif n != 0 and x == 0:
        answer = str(n)
    elif n != 0 and x == 1:
        answer = str(x) + 'x' +str(n)
        answer = answer.replace('1x', 'x + ')
    elif n != 0 and x != 0:
        answer = str(x)+'x' + str(n)
        answer = answer.replace('x', 'x + ')
    return answer