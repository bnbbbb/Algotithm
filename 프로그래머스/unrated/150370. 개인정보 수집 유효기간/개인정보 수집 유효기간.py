def solution(today, terms, privacies):
    answer = []
    today = today.split('.')
    terms = {i.split()[0]: int(i.split()[1]) for i in terms}
    for idx, date in enumerate(privacies, 1):
        date = date.replace(' ', '.')
        date = date.split('.')
        year, mon, day = int(date[0]), int(date[1]), int(date[2])
        mon += terms[date[-1]]
        day -= 1
        if day == 0: 
            day = 28
            mon -= 1
        while True:

            if mon >12:
                year+=1
                mon = mon-12
            else:
                break    
        if int(today[0]) > year:
            answer.append(idx)
            continue
        elif int(today[0]) == year and int(today[1]) > mon:
            answer.append(idx)
            continue
        elif int(today[0]) == year and int(today[1]) == mon and int(today[2]) > day:
            answer.append(idx)
            continue
    return answer