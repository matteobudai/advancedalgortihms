# Python implementation for Kruskal's algorithm

# Find set of vertex a
def find(a):
    while parent[a] != a:
        a = parent[a]
    return a

# Does union of a and b. It returns
# false if a and b are already in same
# set.
def union(a, b):
    node1 = find(a)
    node2 = find(b)
    parent[node1] = parent[node2]

def kruskalMST(cost):
    costTotal = 0 

    # Initialize sets of disjoint sets
    for node in range(numNodes):
        parent[node] = node

    # Include minimum weight edges one by one
    edge = 0
    while edge < numNodes - 1:
        min = INF
        a = -1
        b = -1
        for i in range(numNodes):
            for j in range(numNodes):
                if find(i) != find(j) and cost[i][j] < min:
                    min = cost[i][j]
                    a = i
                    b = j
        union(a, b)
        print("Edge " + str(edge) + ": (" + str(a) + "," + str(b) + ")" + " cost:" + str(min))
        edge += 1
        costTotal += min
    print("Minimum cost= " + str(costTotal))
    return costTotal
