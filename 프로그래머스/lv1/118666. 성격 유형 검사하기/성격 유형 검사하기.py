def solution(survey, choices):
    point = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    cell = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0,} 
    answer = ''
    for i in range(len(choices)):
        if choices[i] < 4:
            cell[survey[i][0]] += point[choices[i]]
        elif choices[i] > 4:
            cell[survey[i][1]] += point[choices[i]]
    for i in range(0, len(cell), 2):
        if list(cell.values())[i] > list(cell.values())[i+1]:
            answer += list(cell.keys())[i]
        elif list(cell.values())[i] < list(cell.values())[i+1]:
            answer += list(cell.keys())[i+1]
        else:
            answer += list(cell.keys())[i] if list(cell.keys())[i] < list(cell.keys())[i+1] else list(cell.keys())[i+1]
            
        

    return answer