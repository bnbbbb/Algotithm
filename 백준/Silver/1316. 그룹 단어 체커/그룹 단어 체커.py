def group_word(word):
    count = 0
    is_group_word = True
    visited = set()
    
    for i in range(len(word)):
        if word[i] in visited and word[i] != word[i-1]:
            return 0
        visited.add(word[i])
    if is_group_word:
        count +=1
    return count

N = int(input())
count = 0
for _ in range(N):
    S = input()
    count += group_word(S)
print(count)