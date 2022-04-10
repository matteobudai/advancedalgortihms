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
def find(a, parent):
    print(a)
    print(parent)
    while parent[a-1] != a:
        a = parent[a-1]
    return a

# Does union of a and b. It returns
# false if a and b are already in same
# set.
def union(a, b, parent):
    node1 = find(a, parent)
    node2 = find(b, parent)
    parent[node1-1] = parent[node2-1]

def Kruskal(costs):
  totalCost = 0
  numNodes = costs[0]
  print(costs)
  parent = [node for node in range(1, numNodes+1)]
  costs = costs[1:]
  costs.sort() # sort list of edges by weight
  for edges in costs:
    if find(edges[1], parent) != find(edges[2], parent):
      union(edges[1], edges[2], parent)
      totalCost += edges[0]
  return totalCost

results = []
results_xplot = []
results_yplot = []
results_zplot = []
count_files = 0

for filepath in glob.iglob('mst_dataset//*.txt'):
    print(filepath)
    start = time.time()
    new = Graph()
    points = new.buildGraph(open(filepath, "r"))
    numNodes = new.numNodes(open(filepath, "r"))
    costs = [numNodes]+points
    mst = Kruskal(costs)
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
