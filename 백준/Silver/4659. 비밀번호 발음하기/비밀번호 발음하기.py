def condition_one(vowels, consonant, word):
    for vowel in vowels:
        if vowel in word:
            result = True
            return condition_two(vowels, consonant, word, result)

def condition_two(vowels, consonant, word, c1):
    if not c1:
        return False
    v_count = 1
    c_count = 1
    for i in range(1, len(word)):
        if v_count == 3 or c_count == 3:
            return False
        elif word[i-1] in vowels and word[i] in vowels:
            v_count += 1
        elif word[i-1] in vowels and word[i] in consonant:
            v_count = 1
        elif word[i-1] in consonant and word[i] in consonant:
            c_count += 1
        elif word[i-1] in consonant and word[i] in vowels:
            c_count = 1
    result = False if v_count == 3 or c_count == 3 else True
    return condition_three(word, result)

def condition_three(word, c2):
    if not c2:
        return False
    result = [word[0]]
    exclude_word = set(['ee', 'oo'])
    duplication = set()
    for i in range(1, len(word)):
        if (word[i] == word[i-1]):
            duplication.add(''.join([word[i-1], word[i]]))
    answer = duplication.difference(exclude_word)
    return False if answer else True

consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']
while True:
    word = input()
    if word == 'end':
        break
    else:
        result = condition_one(vowels, consonant, word)
        if result == True:
            print(f'<{word}> is acceptable.')
        else:
            print(f'<{word}> is not acceptable.')