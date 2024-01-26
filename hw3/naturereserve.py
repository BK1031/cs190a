def find(component_dict, x):
    if component_dict[x] != x:
        component_dict[x] = find(component_dict, component_dict[x])
    return component_dict[x]

def unite(component_dict, p, q):
    root_p = find(component_dict, p)
    root_q = find(component_dict, q)
    component_dict[root_p] = root_q

def kruskal(edges, n):
    edges.sort()
    mst_cost = 0
    component_dict = {i: i for i in range(n)}

    for weight, (u, v) in edges:
        if find(component_dict, u) != find(component_dict, v):
            mst_cost += weight
            unite(component_dict, u, v)

    return mst_cost

data_sets = int(input())
for _ in range(data_sets):
    N, M, L, S = map(int, input().split())
    edges = [(0, (-1, 0))] * (S + M)

    for i in range(S):
        edges[i] = (0, (int(input()), 0))

    for i in range(M):
        u, v, w = map(int, input().split())
        edges[S + i] = (w, (u, v))

    result = kruskal(edges, N + 1) + (N - S) * L
    print(result)
