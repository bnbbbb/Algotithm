import sys

def solution(n, your_id, k, test, m):
    teams = {}
    for i in range(1, n+1):
        teams[i] = {'score': 0, 'problems': {j: 0 for j in range(1, k+1)}, 'submissions': 0, 'lasttime': 0}
    for i in range(m):
        teams[test[i][0]]['problems'][test[i][1]] = max(teams[test[i][0]]['problems'][test[i][1]], test[i][2])
        teams[test[i][0]]['submissions'] += 1
        teams[test[i][0]]['lasttime'] = i + 1

    for team_id, team_info in teams.items():
        teams[team_id]['score'] = sum(team_info['problems'].values())
        
    sorted_teams = sorted(teams.items(), key = lambda x : ((-x[1]['score'], x[1]['submissions']), x[1]['lasttime']))
    
    for idx, (team_id, _) in enumerate(sorted_teams, 1):
        if your_id == team_id:
            print(idx)


input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, k, id, m = map(int, input().split())
    test = [list(map(int, input().split())) for _ in range(m)]
    solution(n, id, k, test, m)