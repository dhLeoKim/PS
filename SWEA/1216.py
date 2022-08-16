# row 방향 j와 k 사이 구간의 회문 체크
def checkRow(lst, i, j, k):
    while j < k:
        if lst[i][j] != lst[i][k]: return False
        j += 1
        k -= 1
    return True

# col 방향 j와 k 사이 구간의 회문 체크
def checkCol(lst, i, j, k):
    while j < k:
        if lst[j][i] != lst[k][i]: return False
        j += 1
        k -= 1
    return True

T = 10
for case in range(T):
    tc = int(input())
    lst = [list(input()) for _ in range(100)]
    N = len(lst)
    max_len = 1
    for i in range(N):
        for j in range(N):
            # 회문의 최대길이 이하는 검사하지 않음
            for k in range(j+max_len, N):
                # 회문 체크, 회문이라면 최대길이는 j와 k의 거리
                if lst[i][j] == lst[i][k] and checkRow(lst, i, j+1, k-1) == True:
                    max_len = k - j + 1
                if lst[j][i] == lst[k][i] and checkCol(lst, i, j+1, k-1) == True:
                    max_len = k - j + 1

    print(f'#{case+1} {max_len}')