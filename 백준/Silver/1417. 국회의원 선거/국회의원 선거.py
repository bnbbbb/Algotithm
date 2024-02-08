def buy_member(n, members):
    me = members[0]
    members = members[1:]
    count = 0
    if n == 1:
        return 0
    
    while me <= max(members):
        members.sort(reverse=True)
        me += 1
        members[0] -= 1
        count += 1
    return count 
n = int(input())

members = [int(input()) for _ in range(n)]

print(buy_member(n, members))