num = {2:['A','B','C'], 3:['D','E', 'F'], 4:['G','H','I'],
    5:['J','K','L'], 6:['M','N','O'], 7:['P','Q','R','S'],
    8:['T','U','V'], 9:['W','X','Y','Z']}
time = 0
word = list(input())
for j in word:
    for key, value in num.items():
        if j in value:
            time += (key + 1)
print(time)