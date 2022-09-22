import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w.sort(reverse=True)
    t.sort(reverse=True)

    ret = 0
    used = [False]*len(w)
    for i in t:
        for j in range(len(w)):
            if not used[j] and i >= w[j]:
                used[j] = True
                ret += w[j]
                break

    print(f'#{case} {ret}')