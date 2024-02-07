def dna_count(n, m, dna):
    result = []
    total = 0
    for i in range(m):
        dna_dict = {'A':0, 'C':0, 'G':0, 'T':0 }
        for j in range(n):
            dna_dict[dna[j][i]] += 1
            
        max_key = max(dna_dict, key = dna_dict.get)
        total += n - dna_dict[max_key]
        
        result.append(max_key)
        
    return total, result
n, m = map(int, input().split())

dna = [list(input()) for _ in range(n)]
total, result = dna_count(n, m, dna)
print(''.join(result))
print(total)