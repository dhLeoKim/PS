import sys
sys.stdin = open('input_4615.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = []
    for _ in range(M):
        i, j, p = map(int, input().split())
        lst.append([i-1, j-1, p])

    board = [[0]*N for _ in range(N)]
    board[N//2][N//2] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    board[N//2-1][N//2-1] = 2

    di, dj = [1, 0, -1, 0, 1, 1, -1, -1], [0, 1, 0, -1, 1, -1, 1, -1]

    for t in range(M):
        i, j, p = lst[t]
        board[i][j] = p
    
        stack = []
        for k in range(8):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] != p and board[ni][nj] != 0:
                stack.append((ni, nj, k))

        temp = []
        while stack:
            i, j, k = stack.pop()
            temp.append((i, j))
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 0 :
                    temp = []
                elif board[ni][nj] == p :
                    for i, j in temp:
                        board[i][j] = p
                    temp = []
                else:
                    stack.append((ni, nj, k))
            else:
                temp = []
        
    p1 = p2 = 0
    for row in board:
        for p in row:
            if p == 1:
                p1 += 1
            elif p == 2:
                p2 += 1

    print(f'#{tc}', p1, p2)