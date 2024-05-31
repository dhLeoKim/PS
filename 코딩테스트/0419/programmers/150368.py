def solution(users, emoticons):
    
    N = len(users)
    M = len(emoticons)
    dc = [10, 20, 30, 40]
    lst = []
    ret = [0, 0]

    def dfs(idx):
        nonlocal ret
        if idx == M:
            tmp = [0 , [0]*N]
            for j in range(N):
                for k in range(M):
                    if users[j][0] <= lst[k][0]:
                        tmp[1][j] += lst[k][1]
                
                if tmp[1][j] >= users[j][1]:
                    tmp[0] += 1
                    tmp[1][j] = 0

            tmp[1] = sum(tmp[1])
            if tmp[0] >= ret[0] and tmp[1] > ret[1]:
                ret = tmp
            elif tmp[0] > ret[0]:
                ret = tmp
            return 
        
        for i in range(4):
            lst.append([dc[i], int(emoticons[idx]*(100-dc[i])/100)])
            dfs(idx+1)
            lst.pop()

    dfs(0)

    return ret

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]

print(solution(users, emoticons))