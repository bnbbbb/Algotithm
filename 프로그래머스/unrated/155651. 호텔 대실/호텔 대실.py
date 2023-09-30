def solution(book_time):
    book_time.sort()  
    rooms = []  
    answer = 0
    
    for start, end in book_time:
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        
        start_time = start_h * 60 + start_m
        end_time = end_h * 60 + end_m
        
        available_room = False
        for i, room in enumerate(rooms):
            if room <= start_time:
                rooms[i] = end_time + 10  
                available_room = True
                break
        if not available_room:
            rooms.append(end_time + 10)  
            answer += 1  
    
    return answer