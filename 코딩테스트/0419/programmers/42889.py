def solution(N, stages):
    user_num = [0]*(N+2)
    for i in stages:
        user_num[i] += 1

    clear_num = [0]*(N+2)
    clear_num[0] = len(stages)
    for i in range(1, len(user_num)):
        clear_num[i] = clear_num[i-1] - user_num[i]

    failure = [0]*N
    for i in range(N):
        if clear_num[i] == 0:
            failure[i] = 0
        else:
            failure[i] = user_num[i+1]/clear_num[i]

    idx = list(range(1, N+1))
    temp = [[x, y] for x, y in zip(idx, failure)]
    temp.sort(reverse= True, key= lambda x: x[1])

    print(temp)

    answer = []
    for i in temp:
        answer.append(i[0])

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))