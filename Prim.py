import math
import time
from collections import defaultdict
import sys

#Create a node
class Node:
    def __init__(self, tag: int):
        self.tag = tag
        self.key = None
        self.parent = None
        self.isPresent = True
        self.index = tag-1 # Track the index of the node in the heap instead of using list.index() method which is O(n)
        self.adjacencyList = []
    
    # For test
    def print(self):
        print("tag =", self.tag, "adjList=", self.adjacencyList, "key=", self.key)

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
    def __init__(self):
        return 0 #complete
       
    def parent(self, pos):
        return pos//2

    def left(self, k):
        return 2 * k + 1

    def right(self, k):
        return 2 * k + 2
    
    

def Prim (G: Graph, s: Node):
    start=time.time()
    for u in G.nodes.values():
        u.key= math.inf
    s.key = 0
    Q= MinHeap #complete
    while Q.heapSize != 0:
        u=MinHeap.extractMin() #complete
        for V in u.adjacencyList:
            if V[0].isPresent() and V[1]<V[0].key:
                V[0].key=V[1]
                V[0].parent= u
                #property to mantain MinHeap
    print("Start = node", s.tag,"\nPrim execution time =", time.time() - start)


start = time.time()
startingNode = 1 # Root node tag
new = Graph()
new.buildGraph(open("mst_dataset/input_random_01_10.txt", "r"))









   

    

    
