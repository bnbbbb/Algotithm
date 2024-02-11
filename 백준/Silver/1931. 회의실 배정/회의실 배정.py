import sys

def meeting(meetings):
    meetings.sort(key=lambda x: (x[1], x[0]))
    selected_meetings = []
    end_time = 0
    
    for meeting in meetings:
        if meeting[0] >= end_time:
            selected_meetings.append(meeting)
            end_time = meeting[1]
    return selected_meetings

n = int(input())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

select_meeting = meeting(meetings)
print(len(select_meeting))
