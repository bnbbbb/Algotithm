from itertools import combinations

def solution(orders, course):
    answer = []
    
    for i in course:
        candidates = {}
        
        for order in orders:
            # 각 주문에서 길이가 i인 조합 생성
            order_combinations = list(combinations(order, i))
            
            for combo in order_combinations:
                # 조합을 알파벳 순서로 정렬하여 딕셔너리에 추가
                sorted_combo = ''.join(sorted(combo))
                if sorted_combo in candidates:
                    candidates[sorted_combo] += 1
                else:
                    candidates[sorted_combo] = 1
        
        # 후보 메뉴 중 가장 많이 주문된 메뉴 찾기
        max_count = 2  # 최소 2번 이상 주문된 메뉴만 고려
        for menu, count in candidates.items():
            if count >= max_count:
                max_count = count
        
        # 가장 많이 주문된 메뉴들 추가
        for menu, count in candidates.items():
            if count == max_count:
                answer.append(menu)
    
    # 알파벳 순서대로 정렬
    answer.sort()
    
    return answer
