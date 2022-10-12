import sys
sys.stdin = open('input_4340.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    pipe = {
        1: [1, 3],
        2: [0, 2],
    }

    pipe_nxt = {
        1: [1, 4, 5],
        2: [2, 5, 6],
        3: [1, 4, 5],
        4: [2, 5, 6],
        5: [2, 5, 6],
        6: [1, 4, 5],
    }

    # 하, 우, 상, 좌
    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]

    print(f'#{tc}')