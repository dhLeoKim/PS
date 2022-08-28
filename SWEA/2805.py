import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    N = int(input())
    lst = [list(map(int, list(input()))) for _ in range(N)]

    ret = 0
    k = 0
    for i in range(N//2+1):
        ret += sum(lst[i][N//2-k:N//2+1+k])
        k += 1

    k -= 1
    for i in range(N//2+1, N):
        k -= 1
        ret += sum(lst[i][N//2-k:N//2+1+k])

    print(f'#{case+1} {ret}')
