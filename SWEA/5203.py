import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    lst = list(map(int, input().split()))

    c1 = [0]*12
    c2 = [0]*12
    p1 = p2 = 0
    ret = 0
    for i in range(0, len(lst), 2):
        c1[lst[i]] += 1
        for j in range(10):
            if c1[j] == 3 or (c1[j] and c1[j+1] and c1[j+2]):
                ret = 1
        if ret: break

        c2[lst[i+1]] += 1
        for j in range(10):
            if c2[j] == 3 or (c2[j] and c2[j+1] and c2[j+2]):
                ret = 2
        if ret: break

    else:
        ret = 0

    print(f'#{case} {ret}')