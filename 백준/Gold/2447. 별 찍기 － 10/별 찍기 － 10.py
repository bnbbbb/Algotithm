def draw_star_pattern(N):
    if N == 3:
        return ["***", "* *", "***"]
    
    smaller_pattern = draw_star_pattern(N // 3)
    blank_line = " " * (N // 3)
    
    result = []
    for line in smaller_pattern:
        result.append(line * 3)
    
    for i in range(N // 3):
        result.append(smaller_pattern[i] + blank_line + smaller_pattern[i])
    
    for line in smaller_pattern:
        result.append(line * 3)
    
    return result

N = int(input())
pattern = draw_star_pattern(N)

for line in pattern:
    print(line)