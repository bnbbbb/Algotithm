import sys
input = sys.stdin.readline

t = int(input()) 
answer = []

for _ in range(t):
    n = int(input())
    applicants = [tuple(map(int, input().split())) for _ in range(n)]
    
    applicants.sort(key=lambda x: x[1])  # 면접 성적을 기준으로 정렬
    min_interview_rank = float('inf')
    count = 0

    for i in range(n):
        if applicants[i][0] < min_interview_rank:
            min_interview_rank = applicants[i][0]
            count += 1
            
    answer.append(count)

print('\n'.join(map(str, answer)))