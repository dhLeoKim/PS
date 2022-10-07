import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    N, W, H = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(H)]

    for row in lst:
        print(row)

    print(f'#{case}')

    

    break