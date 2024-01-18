import sys
input = sys.stdin.readline
t = int(input()) 
answer =[]
for _ in range(t):
    n = int(input()) 
    applicants = [tuple(map(int, input().split())) for _ in range(n)]  
    applicants.sort(key=lambda x: x[0])
    min_interview_rank = float('inf')  
    count = 0  

    for i in range(n):
        if applicants[i][1] < min_interview_rank:
            min_interview_rank = applicants[i][1]
            count += 1
    answer.append(count)

for i in answer:
    print(i)