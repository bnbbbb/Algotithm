def solution(s):
    answer = ''
    string = ''
    dic = {'zero': 0, 'one':1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6
    , 'seven': 7, 'eight': 8, 'nine': 9}
                
    for i, j in dic.items():
        s = s.replace(i, str(j))
    return int(s)

# for i in s:
#     if i.isdigit():
#         answer+= i
#     else:
#         string += i
#         if string in dic:
#             answer += str(dic[string])
#             string = ''