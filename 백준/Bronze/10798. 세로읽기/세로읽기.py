words = [input() for _ in range(5)]
answer = ''
for i in range(15):
    for j in range(5):
        answer += words[j][i:i+1]
print(answer)