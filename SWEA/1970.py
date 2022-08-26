import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    N = int(input())
    change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    
    cnt = [0]*8
    i = 0
    while N > 9:
        if change[i] > N:
            i += 1
            continue
        N -= change[i]
        cnt[i] += 1

    print(f'#{case+1}')
    print(*cnt)