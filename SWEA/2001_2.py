import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    max_ret = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                temp += sum(lst[i+k][j:j+M])
            if temp > max_ret:
                max_ret = temp

    print(f'#{case+1} {max_ret}')