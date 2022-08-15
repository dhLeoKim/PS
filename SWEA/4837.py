T = int(input())

for case in range(T):
    N, K = map(int, input().split())
    A = list(range(1, 13))
    ret = 0
    # 비트연산자로 모든 부분 집합 생성
    for i in range(1 << 12):
        temp = []
        for j in range(12):
            if i & (1 << j):
                temp.append(A[j])
        # 부분집합 결과를 temp에 저장 후
        # temp의 원소 개수가 N이면...
        if len(temp) == N:
            temp_sum = 0
            for s in temp:
                temp_sum += s
            # 원소의 합 K인지 확인, 맞으면 ++
            if temp_sum == K:
                ret += 1

    print(f'#{case+1} {ret}')