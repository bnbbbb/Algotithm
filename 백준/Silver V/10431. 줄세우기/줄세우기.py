def count_steps(heights):
    n = len(heights)
    steps = 0

    for i in range(n):
        taller_than_i = sum(height < heights[i] for height in heights[i+1:])
        steps += taller_than_i

    return steps

def main():
    P = int(input())  # 테스트 케이스의 수

    for _ in range(P):
        case_number, *heights = map(int, input().split())
        total_steps = count_steps(heights)
        print(f"{case_number} {total_steps}")

if __name__ == "__main__":
    main()
    
