import sys
sys.stdin = open('input_1043.txt')
input = sys.stdin.readline

N, M = list(map(int, input().split()))
lst_t = list(map(int, input().split()))[1:]

rep = [i for i in range(N + 1)]
for i in lst_t:
    rep[i] = 0

def find(x):
    if rep[x] != x:
        rep[x] = find(rep[x])
    return rep[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        rep[b] = a
    else:
        rep[a] = b


parties = []
for _ in range(M):
    party = list(map(int, input().split()))[1:]
    for i in range(len(party) - 1):
        union(party[i], party[i + 1])   # 교집합 비교
    parties.append(party)

ret = 0

for party in parties:
    know = False
    for i in range(len(party)):
        if find(party[i]) == 0:         # 진실
            know = True
            break
    if not know:
        ret += 1

print(ret)