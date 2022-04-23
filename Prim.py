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

    def createNodes(self, nums: int):
        for i in range(1, nums+1): # nums+1 in order to cover the last node
            self.nodes[i] = Node(i)
    
    def buildGraph(self, input):
        lines = input.readlines()
        self.createNodes(int(lines[0].split()[0]))
        lines.pop(0) 
        for iterate in range(len(lines)):
            info = list(map(int, lines[iterate].split()))
            self.makeNodes(info[0], info[1], info[2])

    #Create all of the nodes
    def makeNodes(self, tag, adjTag, adjCost):
        self.nodes[tag].adjacencyList.append([self.nodes[adjTag], adjCost])
        self.nodes[adjTag].adjacencyList.append([self.nodes[tag], adjCost])

    #Define number of edges
    def numNodes(self, input):
        lines = input.readlines(0)
        numNodes = int(lines[0].split()[0])
        return numNodes

class ArrayHeap(list):
    def __init__(self, array):
        super().__init__(array)
        self.heapSize = len(array)

class MinHeap:
    def __init__(self, array: list, root: Node):
        self.arrayHeap = ArrayHeap(array)
        
        # Check if the root node is not the first
        # If it is not, reset the starting node by
        # removing the root node from it's original position
        # inserting it in the first position
        # and then update all indexes
        if self.arrayHeap[0] != self.arrayHeap[root.tag-1]: 
            rootNode = self.arrayHeap[root.tag-1]
            self.arrayHeap.remove(rootNode)
            self.arrayHeap.insert(0,rootNode)
            for i in range(0,self.arrayHeap.heapSize):
                self.arrayHeap[i].index = i

    def getParentIndex(self,index):
        if index%2 == 0: 
            return index//2 - 1
        else:
            return index//2

    def getLeftChildIndex(self,index):
        return 2*index+1

    def getRightChildIndex(self,index):
        return 2*index+2

    def minHeapify(self,i):
        #minHeapify is always called after we call extractMin(), in order to maintain the min heap structure
        #we always call minHeapify() FIRST with node 0, then it checks if it needs to perform a swap with the 
        #left or right child, and if so it calls minHeapify() on the newly swapped min node until nodes are arranged properly 
        #such that the root node is smaller than it's children
        #if node 0 is already the minimum node then a swap is not performed 
        l = self.getLeftChildIndex(i)
        r = self.getRightChildIndex(i)
        if l <= self.arrayHeap.heapSize-1 and self.arrayHeap[l].key < self.arrayHeap[i].key:
            min = l
        else:
            min = i
        if r <= self.arrayHeap.heapSize-1 and self.arrayHeap[r].key < self.arrayHeap[min].key:
            min = r
        if min != i:
            self.arrayHeap[i].index, self.arrayHeap[min].index = min, i # Update indexes
            self.arrayHeap[i], self.arrayHeap[min] = self.arrayHeap[min], self.arrayHeap[i]
            self.minHeapify(min)

    def shiftUp(self, index):
        parent = self.getParentIndex(index)
        current = index
        while current > 0 and self.arrayHeap[parent].key > self.arrayHeap[current].key:
            self.arrayHeap[current].index, self.arrayHeap[parent].index = parent, current # Update indexes
            self.arrayHeap[current], self.arrayHeap[parent] = self.arrayHeap[parent], self.arrayHeap[current]
            current = parent
            parent = self.getParentIndex(parent)

    def extractMin(self):
        #this function both extracts the min and pops it out of the min heap
        # in a min heap data structure, the root node at index 0 will always be the priority(minimum) 
        #so we extract the node at index zero and define it as the min to pass back
        min=self.arrayHeap[0]
        self.arrayHeap[0].isPresent = False
        #then swap the right most node and first(min) node
        self.arrayHeap[0], self.arrayHeap[self.arrayHeap.heapSize-1] = self.arrayHeap[self.arrayHeap.heapSize-1], self.arrayHeap[0]
        self.arrayHeap[0].index = 0
        #reduce the heapSize by 1 to pop out the min node
        self.arrayHeap.heapSize -=1
        #finally call minheapify() to restructure/maintain the min heap data structure
        self.minHeapify(0)
        return min
        
    
#Algorithm
def Prim (G: Graph, s: Node):
    start=time.time()  
    for u in G.nodes.values():
         u.key= math.inf
    s.key = 0
    MST = 0
    Q = MinHeap(list(G.nodes.values()), s)
    while Q.arrayHeap.heapSize != 0:
        u=Q.extractMin()
        for v in u.adjacencyList:
            if v[0].isPresent and v[1] < v[0].key:
                #if v[0].key is less than infinity it implies it has already been visited and added to the MST
                #we will remove v[0]key, redefine it has v[1], and replace it's value in the MST
                if v[0].key < math.inf:
                    MST -= v[0].key
                v[0].parent = u
                v[0].key = v[1]
                Q.shiftUp(v[0].index)   
                MST += v[0].key
    end=time.time()
    return MST          
