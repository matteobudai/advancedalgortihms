#missing connection with .txt files
#still checking if I can use the while based on node count rather than edges checked
#need to make I am correctly measuring run execution time performance 

from ast import List
import time 
start_time = time.time()

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
    def minCostConnectPoints(self, points) -> int:
        #set n equal to number of edges, nodes = number of nodes
        nodes = 10
        n = len(points)
        all_edges = []
        
        # create list of all edges in complete graph.
        for curr_node in range(n): 
            all_edges.append((points[curr_node][0], points[curr_node][1], points[curr_node][2]))
       
        # Sort all edges in increasing order of weight (column 2)
        all_edges.sort(key=lambda x: x[2])
    
        uf = UnionFind(n)
        mst_weight = 0
        ##edges_used = 0
        nodes_in_MST = 0

        while nodes_in_MST != nodes - 1:
        ##while edges_used != n-1:
            for u, v, weight in all_edges:
                if uf.union(u, v):
                    mst_weight += weight
                    ##edges_used += 1
                    nodes_in_MST += 1
            return mst_weight
            
        

List_G = [
(1, 2, 4188),
(2, 3, -4502),
(3, 4, 6938),
(3, 5, 6937),
(4, 5, 3256),
(5, 6, 7605),
(6, 7, 8856),
(7, 8, -7786),
(8, 9, 9244),
(8, 4, 5906),
(9, 10, 7091),
(9, 6, -5756)]

mst = Solution()
print(mst.minCostConnectPoints(List_G)) 
print("--- %s seconds ---" % (time.time() - start_time))