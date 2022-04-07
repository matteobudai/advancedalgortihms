import math
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import defaultdict
import time 
import glob


#Create a node
class Node:
    def __init__(self, tag: int):
        self.tag = tag
        self.key = None
        self.parent = None
        self.isPresent = True
        self.index = tag-1 
        self.adjacencyList = []

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
            info_int.append([int(info[i][0]), int(info[i][1]), int(info[i][2])])
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
    numNodes = cost[0]
    print(cost)
    parent = [node for node in range(numNodes)]
    costs = []
    for iterate in range(numNodes):
        costs.append([INF]*numNodes)
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
        edge += 1
        costTotal += min
    #print("Minimum cost= " + str(costTotal))
    return costTotal


INF = float('inf')
results = []
results_xplot = []
results_yplot = []
results_zplot = []
count_files = 0

for filepath in glob.iglob('mst_dataset//*.txt'):
    start = time.time()
    new = Graph()
    points = new.buildGraph(open(filepath, "r"))
    numNodes = new.numNodes(open(filepath, "r"))
    costs = [numNodes]+points
    mst = kruskalMST(costs)
    end = time.time()
    results.append([numNodes,mst,round(end - start,5)])
    count_files += 1

results.sort(key=lambda x: x[0])

for i in range(1,count_files): 
    results_xplot.append(int(results[i][0]))
    results_yplot.append(float(results[i][2]))


print("\n","Nodes, Cost, Time","\n",results)
print("\n","\n",results_yplot)

z = np.polyfit(results_xplot, results_yplot, 1)
p = np.poly1d(z)
plt.plot(results_xplot, results_yplot)
plt.plot(results_xplot,p(results_xplot),"r--")
plt.title('Kruskal - Union Find')
plt.ylabel('Execution time (s)')
plt.xlabel('# of Vertices')
plt.ylim(0,.15)
plt.show()
