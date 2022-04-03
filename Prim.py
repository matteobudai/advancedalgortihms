import math
import time
from collections import defaultdict

#Create a node
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
        self.numNodes(int(lines[0].split()[0]))
        lines.pop(0) 
        for iterate in range(len(lines)):
            info = list(map(int, lines[iterate].split()))
            print(info)
            self.makeNodes(info[0], info[1], info[2])

    #Create number of vertices
    def numNodes(self, vertices):
        for iterate in range(1, vertices+1):
            self.nodes[iterate] = Node(iterate)
    
    #Create all of the nodes
    def makeNodes(self, tag, adjTag, adjCost):
        self.nodes[tag].adjacencyList.append([self.nodes[adjTag], adjCost])
        self.nodes[adjTag].adjacencyList.append([self.nodes[tag], adjCost])


class ArrayHeap(list):
    def __init__(self, array):
        super().__init__(array)
        self.heapSize = len(array)

class MinHeap:
    def __init__(self, array: list, root: Node):
        self.arrayHeap = ArrayHeap(array)
        # Check if the root node is not the first
        if self.arrayHeap[0] != self.arrayHeap[root.tag-1]: # reset the starting node and update all indexes
            rootNode = self.arrayHeap[root.tag-1]
            self.arrayHeap.remove(rootNode)
            self.arrayHeap.insert(0,rootNode)
            for i in range(0,self.arrayHeap.heapSize):
                self.arrayHeap[i].index = i

    def getParentIndex(self,index):
        return (index-1)//2

    def getLeftChildIndex(self,index):
        return 2*index+1

    def getRightChildIndex(self,index):
        return 2*index+2

    def hasParent(self,index):
        return self.getParentIndex(index)>=0

    def swap(self, left, right):
        self.arrayHeap[left], self.arrayHeap[right] = self.arrayHeap[right], self.arrayHeap[left]

    def minHeapify(self, i):
        l = self.getLeftChildIndex(i)
        r = self.getRightChildIndex(i)
        print('complete')

    def extractMin(self):
        print('complete')
    
    
   
#Algorithm
def Prim (G: Graph, s: Node):
    start=time.time()  
    for u in G.nodes.values():
         u.key= math.inf
    s.key = 0
    Q = MinHeap(list(G.nodes.values()), s)
    while Q.arrayHeap.heapSize != 0:
        u=Q.extractMin()
        for v in u.adjacencyList:
            if v[0].isPresent and v[1] < v[0].key:
                v[0].parent = u
                v[0].key = v[1]                
    end=time.time()
    print("Start = node", s.tag,"\nPrim execution time =", end - start)



start = time.time()
startingNode = 1 # Root node tag
new = Graph()
new.buildGraph(open("mst_dataset/input_random_02_10.txt", "r"))
Prim(new, new.nodes.get(startingNode))
end = time.time()
print("Program execution time =", end - start)
sum = 0
for node in new.nodes.values():
    sum += node.key
print("Final cost =",sum, "\n")









   

    

    
