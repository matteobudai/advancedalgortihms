import time 
import glob
import matplotlib.pyplot as plt
import numpy as np

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


class UnionFind:
    def __init__(self, nodes_G) -> None:   
        #initialize each node to belong to a group of itself 
        self.group = [i for i in range(nodes_G+1)]
        #initialize the rank of each group to be constant 0
        self.rank =  [0 for _ in range(nodes_G+1)]
         
    def find(self, node) -> int:
        #find and return the group that the node belongs to: 
        #   if the node does not belong in it's own set (as originally initilized)
        #   then traverse nodes in it's belonging group until finding the parent node
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def union(self, u, v) -> bool:
        #first find groups for u and v
        group_u = self.find(u)
        group_v = self.find(v)
        
        # if node u and v already belong to same group then do nothing
        if group_u == group_v:
            return False
        
        #if node u and v belong to different groups and
        #   group u has a higher rank than group v, set the group for all nodes group v equal to group u
        if self.rank[group_u] > self.rank[group_v]:
            self.group[group_v] = group_u
        #   group v has a higher rank than group u (also applies to first check where the rank is equal), 
        #   set the group for all nodes in group u equal to group v, and increase the ranking of group v
        else:
            self.group[group_u] = group_v
            self.rank[group_v] += 1
        return True
       
    
class Solution:
    def KruskalUF(self, points, numNodes) -> int:
        
        #read in graph and calculate length to determine number of edges
        all_edges = points
        n = len(points)

        # Sort all edges in non-decreasing order of weight (column 2)
        all_edges.sort(key=lambda x: x[2])
        
        #define Union Find data structure for all nodes
        uf = UnionFind(numNodes)
        mst_weight = 0
        edges_used = 0
        
        while edges_used != n-1: 
            for u, v, weight in all_edges:
                if uf.union(u, v):
                    mst_weight += weight
                    edges_used += 1
            return mst_weight


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
    mst = Solution()
    end = time.time()
    results.append([numNodes,mst.KruskalUF(points,numNodes),round(end - start,5)])
    count_files += 1

results.sort(key=lambda x: x[0])

for i in range(1,count_files): 
    results_xplot.append(int(results[i][0]))
    results_yplot.append(float(results[i][2]))


N = len(results_xplot)
x2 = np.arange(N)

#plt.set_xticks(results_xplot)
plt.plot(x2, results_yplot)
plt.title('Kruskal - Union Find')
plt.ylabel('Execution time (s)')
plt.xlabel('# of Vertices')
plt.xticks(x2,results_xplot)
plt.tick_params(axis='x', labelrotation=90) 
plt.ylim(0,0.18)
plt.show()

