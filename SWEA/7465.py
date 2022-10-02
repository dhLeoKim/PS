import sys
sys.stdin = open('s_input.txt')

def find(x):
    while p[x] != x:
        x = find(p[x])
    return x

T = int(input())
for case in range(1, T+1):
    N, M = map(int, input().split())
    lst = [tuple(map(int, input().split())) for _ in range(M)]

    p = [i for i in range(N+1)]

    for x, y in lst:
        p[find(y)] = find(x)

    for i in range(1, N+1):
        p[i] = find(p[i])

    print(f'#{case}', len(set(p[1:])))