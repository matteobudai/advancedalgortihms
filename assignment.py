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
    
    #Convert text to lists of strings
    def txt_to_data(self, fileA):
        with open(fileA, 'r') as infile:
            data = infile.readlines()
            for i in data:
                i = i.split()
            self.numNodes(i[0])
            i.pop(0)
            for iterate in range(len(i)):
                info = list(map(int, i[iterate])) # Convert all the strings deriving from split to int
                self.addNode(info[0], info[1], info[2])

    #Get number of vertices
    def numNodes(self, num):
        for iterate in range(num):
            self.nodes[iterate] = Node(iterate)
    
    #Create all of the nodes
    def makeNode(self, tag, adjTag, adjCost):
        self.nodes[tag].adjacencyList.append([self.nodes[adjTag], adjCost])
        self.nodes[adjTag].adjacencyList.append([self.nodes[tag], adjCost])

    

new = Graph()
lists = new.txt_to_data('input_random_01_10 copia.txt')
