#missing connection with .txt files
#still checking if I can use the while based on node count rather than edges checked
#need to make I am correctly measuring run execution time performance 

from ast import List
import time 
from collections import defaultdict

start_time = time.time()

class Node:
    def __init__(self, tag: int):
        self.tag = tag
        self.key = None
        self.parent = None
        self.isPresent = True
        self.index = tag-1 # Track the index of the node in the heap instead of using list.index() method which is O(n)
        self.adjacencyList = []

#Create a graph
class Graph:
    def __init__(self):
        self.nodes = defaultdict(Node)

    def buildGraph(self, input):
        lines = input.readlines()
        numEdges = int(lines[0].split()[1])
        lines.pop(0) 
        info = []
        info_int = []
        for iterate in range(len(lines)):
            info.append(lines[iterate].split())
        for i in range(0,numEdges): 
            info_int.append([int(info[i][0]), int(info[i][1]), int(info[i][2])])
        return info_int


    #Create number of edges
    def numEdges(self, input):
        lines = input.readlines(0)
        numEdges = int(lines[0].split()[1])
        return numEdges

    #Create number of vertices
    def numNodes(self, vertices):
        for iterate in range(1, vertices+1):
            self.nodes[iterate] = Node(iterate)
    
    #Create all of the nodes
    def makeNodes(self, tag, adjTag, adjCost):
        self.nodes[tag].adjacencyList.append([self.nodes[adjTag], adjCost])
        self.nodes[adjTag].adjacencyList.append([self.nodes[tag], adjCost])

class UnionFind:
    def __init__(self, nodes_G) -> None:
        
        #initialize each node to belong to a group of itself 
        self.group = [i for i in range(nodes_G)]
        
        #initialize the rank of each group to be constant 0
        self.rank =  [0 for _ in range(nodes_G)]
         
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
    def KruskalUF(self, points) -> int:
        
        all_edges = []
        n = len(points)
        # create list of all edges in complete graph.
        for curr_node in range(n): 
            all_edges.append([points[curr_node][0], points[curr_node][1], points[curr_node][2]])
       
        # Sort all edges in increasing order of weight (column 2)
        all_edges.sort(key=lambda x: x[2])
        
        uf = UnionFind(n)
        mst_weight = 0
        edges_used = 0
        

        #while nodes_in_MST != nodes - 1:
        while edges_used != n-1:
            for u, v, weight in all_edges:
                if uf.union(u, v):
                    mst_weight += weight
                    edges_used += 1
                    #nodes_in_MST += 1
            return mst_weight
            
        

#start = time.time()

#startingNode = 1 # Root node tag
new = Graph()
points = new.buildGraph(open("mst_dataset/input_random_02_10.txt", "r"))
#print(points)
numEdges = new.numEdges(open("mst_dataset/input_random_02_10.txt", "r"))
#print(numEdges)
mst = Solution()
mst.KruskalUF(points)
'''
end = time.time()
print("Program execution time =", end - start)
sum = 0
for node in new.nodes.values():
    sum += node.key
print("Final cost =",sum, "\n")
'''