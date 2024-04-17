import sys
sys.stdin = open('input_1018.txt')
input = sys.stdin.readline

# 최악의 경우 8x8 2중 for문 확인을 42번해야함
# 64*42 -> 부루트포스

def chk(si, sj):
    global ret

    temp = 0
    for i in range(7):
        if si+i-1 < 0:
            pass
        elif lst[si+i-1][sj] == lst[si+i][sj]:
            temp += 1
            if lst[si+i-1][sj] == 'B':
                lst[si+i][sj] == 'W'
            elif lst[si+i-1][sj] == 'W':
                lst[si+i][sj] == 'B'

        for j in range(7):
            if lst[si+i][sj+j] == lst[si+i][sj+j+1]:
                temp += 1
                if lst[si+i][sj+j] == 'B':
                    lst[si+i][sj+j+1] = 'W'
                elif lst[si+i][sj+j] == 'W':
                    lst[si+i][sj+j+1] = 'B'
        
    if ret > temp:
        ret = temp


N, M = map(int, (input().split()))
lst = [list(input().strip()) for _ in range(M)]

ret = 1e11
for si in range(M-7):
    for sj in range(N-7):
        if lst[si][sj] == 'B':
            chk(si, sj)
            lst[si][sj] = 'W'
            chk(si, sj)
            lst[si][sj] = 'B'

        elif lst[si][sj] == 'W':
            chk(si, sj)
            lst[si][sj] = 'B'
            chk(si, sj)
            lst[si][sj] = 'W'

print(ret)