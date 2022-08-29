import sys
sys.stdin = open('input.txt')

T = int(input())
T = 55
for case in range(T):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    t = max(lst)
    customer = [0]*(t+1)

    for i in lst:
        customer[i] += 1

    bread = [0]*(t+1)
    for i in range(0, t+1, M):
        bread[i] += K
    bread[0] = 0

    print(f'#{case+1}', end= ' ')

    if customer[0]:
        print('Impossible')
        continue
    else:
        for i in range(1, t+1):
            bread[i] += bread[i-1] - customer[i]

            if bread[i] < 0:
                print('Impossible')
                break
        else:
            print('Possible')