def solution(data, ext, val_ext, sort_by):
    sorted_type = {'code': 0, 'date':1, 'maximum': 2, 'remain': 3}
    result = [d for d in data if d[sorted_type[ext]] < val_ext]
    result = sorted(result, key=lambda x : x[sorted_type[sort_by]])
    return result