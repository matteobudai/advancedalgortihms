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
    def numNodes(self, num):
        for iterate in range(num+1):
            self.nodes[iterate] = Node(iterate)
    
    #Create all of the nodes
    def makeNodes(self, tag, adjTag, adjCost):
        self.nodes[tag].adjacencyList.append([self.nodes[adjTag], adjCost])
        self.nodes[adjTag].adjacencyList.append([self.nodes[tag], adjCost])

new = Graph()
new.buildGraph(open("input_random_01_10 copia.txt", "r"))
