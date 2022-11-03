import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 시간 초과!!!!
###############################################
def bishop(idx, M, ret, arr):
    global max_v, cnt
    cnt += 1

    if idx == M:
        if ret > max_v:
            max_v = ret
        print(arr)
        return

    # elif M-idx-1 + ret <= max_v:
    #     return

    for ii in range(idx, M):
        if M-ii-1 + ret <= max_v:
            return
        i, j = pos[ii]
        if not diag1[i+j] and not diag2[j-i+N-1]:
            diag1[i+j] = True
            diag2[j-i+N-1] = True
            arr.append([i, j])
            bishop(ii+1, M, ret+1, arr)
            diag1[i+j] = False
            diag2[j-i+N-1] = False
            arr.pop()
            # bishop(idx+1, M, ret, arr)

    # bishop(ii+1, M, ret, arr)


N = int(input())
lst = []
pos = []
for i in range(N):
    temp = list(map(int, input().split()))
    lst.append(temp)
    for j in range(N):
        if temp[j]:
            pos.append((i, j))

print(lst)
print(pos)

M = len(pos)
diag1 = [False]*(2*N - 1)
diag2 = [False]*(2*N - 1)
max_v = 0
cnt = 0
bishop(0, M, 0, [])
print(max_v, cnt)