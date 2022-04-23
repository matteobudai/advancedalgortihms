#Create a graph
class Graph:
    #Create list of lists containing all vertices and weights in format [u,v,weight]
    def buildGraph(self, input):
        lines = input.readlines()
        numEdges = int(lines[0].split()[1])
        lines.pop(0) 
        info = []
        info_int = []
        for iterate in range(numEdges):
            info.append(lines[iterate].split())
        for i in range(0,numEdges): 
            info_int.append([int(info[i][2]), int(info[i][0]), int(info[i][1])]) #Changed from original code so that I can use .sort()
        return info_int

    #Create number of edges
    def numEdges(self, input):
        lines = input.readlines(0)
        numEdges = int(lines[0].split()[1])
        return numEdges

    #Create number of edges
    def numNodes(self, input):
        lines = input.readlines(0)
        numNodes = int(lines[0].split()[0])
        return numNodes

# Python implementation for Kruskal's algorithm in a Naive mode

# Find set of vertex a
def search(a, parent):
    while parent[a-1] != a:
        a = parent[a-1]
    return a

# Combines a and b. It returns
# false if a and b are already in same
# set.
def combine(a, b, parent):
    node1 = search(a, parent)
    node2 = search(b, parent)
    parent[node1-1] = parent[node2-1]

def Kruskal(costs):
  totalCost = 0
  numNodes = costs[0]
  parent = [node for node in range(1, numNodes+1)]
  costs = costs[1:]
  costs.sort() # sort list of edges by weight
  for edges in costs:
    if search(edges[1], parent) != search(edges[2], parent):
      combine(edges[1], edges[2], parent)
      totalCost += edges[0]
  return totalCost
