while True:
    a = int(input())
    a_li = [i for i in range(1, a) if a % i == 0]
    a_str = [str(i) for i in a_li]
    if a == -1:
        break
    elif a== sum(a_li):
        result = str(sum(a_li))+' = ' + ' + '.join(a_str)
        print(result)
    else:
        print(f'{a} is NOT perfect.')