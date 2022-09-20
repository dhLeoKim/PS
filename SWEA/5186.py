import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    N = float(input())

    ret = ''
    i = 1
    while N:
        temp = 2**(-i)
        if temp <= N:
            ret += '1'
            N -= temp
        else:
            ret += '0'

        i += 1

    print(f'#{case}', ret if len(ret) <= 12 else 'overflow')