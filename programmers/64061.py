def solution(board, moves):
    board = [list(x) for x in zip(*board)]      # 전치
    n = len(board)
    stack = []
    cnt = 0
    for i in moves:
        for j in range(n):
            p = board[i-1][j]
            if p:                               # 0 이 아니면
                if stack and stack[-1] == p:    # 괄호검사와 동일
                    stack.pop()
                    cnt += 2                    # 사라지는 2개씩 카운트
                else:
                    stack.append(p)    
                board[i-1][j] = 0
                break

    return cnt

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))
