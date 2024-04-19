def find(x):
    if p[x] < 0:
        return x
    return find(p[x])


def union(u, v):
    pu = find(u)
    pv = find(v)
    if p[pu] == p[pv]:
        p[pu] -= 1
    if p[pu] < p[pv]:
        p[pv] = pu
    else:
        p[pu] = pv


def kruskal():
    ret = 0
    for w, u, v in edge:
        if find(u) == find(v):
            continue
        ret += w
        union(u, v)

    return ret


N, E = map(int, input().split())
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append((w, u, v))

edge.sort()
p = [-1]*(N+1)

kruskal()