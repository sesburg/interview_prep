def initialize_parent(num_nodes):
    parent = [0] * num_nodes
    for i in range(num_nodes):
        parent[i] = i
    return parent

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    #make a and b both share the smaller parent
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b
