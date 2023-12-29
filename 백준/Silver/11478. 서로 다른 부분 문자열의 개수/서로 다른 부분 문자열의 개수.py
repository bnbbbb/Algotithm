a = set()
def solution(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            a.add(s[i:j+1])
    return a
s = input()

result = solution(s)
print(len(result))
