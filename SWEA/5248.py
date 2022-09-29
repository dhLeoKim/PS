import sys
sys.stdin = open('sample_input.txt')

def find(x):
    while x != p[x]:
        x = p[x]
    return x

T = int(input())
for case in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    p = [i for i in range(N+1)]

    for i in range(M):
        p[find(lst[2*i+1])] = find(lst[2*i])

    for i in range(1, N+1):
        p[i] = find(i)

    print(f'#{case}', len(set(p[1:])))