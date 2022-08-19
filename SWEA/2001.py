import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    num = []
    for a in range(N-M+1):              # 전체 배열에서
        for b in range(N-M+1):
            temp = 0
            for i in range(a, a+M):     # 파치채 영역 계산
                for j in range(b, b+M):
                    temp += arr[i][j]
            num.append(temp)
    num_max = 0
    for i in num:                       # 최대값 찾기
        if i > num_max: num_max = i

    print(f'#{case+1} {num_max}')