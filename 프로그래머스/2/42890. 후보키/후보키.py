from itertools import combinations

def is_unique(key, relation):
    unique_set = set()
    for row in relation:
        candidate = tuple(row[i] for i in key)
        if candidate in unique_set:
            return False
        unique_set.add(candidate)
    return True

def is_minimal(key, candidate_keys):
    for ck in candidate_keys:
        if set(ck).issubset(set(key)) and key != ck:
            return False
    return True

def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])
    candidate_keys = []

    for num in range(1, col_len + 1):
        for comb in combinations(range(col_len), num):
            key = list(comb)
            if is_unique(key, relation) and is_minimal(key, candidate_keys):
                candidate_keys.append(key)

    return len(candidate_keys)