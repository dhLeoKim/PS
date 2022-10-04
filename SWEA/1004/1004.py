def subsetSum(i, N, s, t):
    global result, cnt
    cnt += 1
    rest_sum = sum(A[i:])
    if i == N:
        if s == t:
            result += 1
        return
    elif s > t:
        return
    elif s + rest_sum < t:
        return
    else:
        subsetSum(i+1, N, s+A[i], t)
        subsetSum(i+1, N, s, t)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0]*len(A)
result = 0
cnt = 0
subsetSum(0, 10, 0, 30)
print(result, cnt)