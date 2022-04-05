# Python implementation for Kruskal's algorithm

# Find set of vertex a
def find(a, parent):
    while parent[a] != a:
        a = parent[a]
    return a

# Does union of a and b. It returns
# false if a and b are already in same
# set.
def union(a, b, parent):
    node1 = find(a, parent)
    node2 = find(b, parent)
    parent[node1] = parent[node2]

def kruskalMST(cost):

    #Create the graph
    numNodes = cost[0][0]
    parent = [node for node in range(numNodes)]
    costs = []
    for iterate in range(numNodes):
        costs.append([INF]*numNodes)
    print(costs)
    for iterate in range(1, len(cost)):
        num1 = cost[iterate][0]-1
        num2 = cost[iterate][1]-1
        costs[num1][num2] = cost[iterate][2]
        costs[num2][num1] = cost[iterate][2]
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
                if find(i, parent) != find(j, parent) and costs[i][j] < min:
                    min = costs[i][j]
                    a = i
                    b = j
        union(a, b, parent)
        print("Edge " + str(edge) + ": (" + str(a) + "," + str(b) + ")" + " cost:" + str(min))
        edge += 1
        costTotal += min
    print("Minimum cost= " + str(costTotal))
    return costTotal

INF = float('inf')
cost = [[10,9], [1,2,4993], [2,3,1392], [3,4,8856], [4,5,-433], [5,6,6590], [6,7,-7462], [7,8,6658], [8,9,-976], [9, 10,9698]]

# Print the solution
kruskalMST(cost)
