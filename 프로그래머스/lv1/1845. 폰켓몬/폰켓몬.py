def solution(nums):
    a = []
    
    for i in nums:
        if i not in a and len(a) < len(nums)//2:
            a.append(i)
    
    return len(a)