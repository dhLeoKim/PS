def solution(brown, yellow):
    N = (brown-4) // 2
    for i in range(N, 0, -1):
        if i*(N-i) == yellow:
            w, h = i+2, N-i+2
            break
        
    return [w, h]

brown = 10
yellow = 2

print(solution(brown, yellow))