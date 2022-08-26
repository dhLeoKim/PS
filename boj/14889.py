import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def checkTeam(i, N):
    if len(t1) == N//2:
        t2 = list(set(team) - set(t1))
        print(t1, t2)
        t1_stat = 0
        for pi in range(len(t1)):
            for pj in range(pi+1, len(t1)):
                t1_stat += lst[t1[pi]][t1[pj]] + lst[t1[pj]][t1[pi]]

        t2_stat = 0
        for pi in range(len(t2)):
            for pj in range(pi, len(t2)):
                t2_stat += lst[t2[pi]][t2[pj]] + lst[t2[pj]][t2[pi]]

        result.append(abs(t1_stat-t2_stat))

    else:
        for j in range(i, N):
            if j in t1: continue
            t1.append(j)
            checkTeam(j, N)
            t1.pop()

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
team = list(range(N))
t1 = [0]
result = []
checkTeam(0, N)
print(result)
print(min(result))