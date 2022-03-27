import math
import time
from collections import defaultdict

# change test 

class Node:
    def __init__(self, tag: int):
        self.tag = tag
        self.key = None
        self.parent = None
        self.isPresent = True
        self.index = tag-1 # Track the index of the node in the heap instead of using list.index() method which is O(n)
        self.adjacencyList = []

class Graph:
    def __init__(self):
        self.nodes = defaultdict(Node)

    def createNodes(self, nums: int):
        for i in range(1, nums+1): # nums+1 in order to cover the last node
            self.nodes[i] = Node(i)

    def addNode(self, tag: int, adjTag: int, adjCost: int):
        self.nodes[tag].adjacencyList.append([self.nodes[adjTag], adjCost])
        self.nodes[adjTag].adjacencyList.append([self.nodes[tag], adjCost]) # Graph is undirected

    def buildGraph(self, input):
        lines = input.readlines()
        self.createNodes(int(lines[0].split()[0])) # Extract number of vertexes and pass it to createNode
        lines.pop(0) # Remove the first line of .txt input file
        for line in lines:
            info = list(map(int, line.split())) # Convert all the strings deriving from split to int
            self.addNode(info[0], info[1], info[2])

def Prim (G: Graph, s: Node):
    start=time.time


start = time.time()
startingNode = 1 # Root node tag
result = Graph()
result.buildGraph(open("mst_dataset/input_random_01_10.txt", "r"))
Prim(result, result.nodes.get(startingNode))
print("Program execution time =", time.time() - start)
sum = 0
for node in result.nodes.values():
    sum += node.key
print("Final cost =",sum, "\n")