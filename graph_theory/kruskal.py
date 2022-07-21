from union_find import *

#edges: list of edges (cost, a, b),
#n_vert: number of of vertices
#return: list of edges used in the mst
def kruskal(edges, n_vert):
    parent = initialize_parent(n_vert)
    edges.sort()
    mst = []
    for e in edges:
        cost, a, b, = e
        if find_parent(parent, a) != find_parent(parent, b):
            mst.append((cost, a, b))
            union_parent(parent, a, b)
    return mst


    
