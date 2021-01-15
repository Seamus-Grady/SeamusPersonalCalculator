import sys
class node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = ''
class mathTree:
    def __init__(self):
        self.root = 0


def buildTheTree(line):
    left = 0
    right = 0
    closingParen = 0
    lineWithoutSpaces = line.split()
    currentProblem = mathTree()
    previousNode = node()
    for i in range(0, len(lineWithoutSpaces)-1):
        currentNode = node()
        if i == 0:
            currentNode.value = lineWithoutSpaces[i]
            currentProblem.root = currentNode
            previousNode = currentNode
            left = 1
        if left == 1:
            currentNode.value = lineWithoutSpaces[i]
            currentProblem.root = currentNode
            currentProblem.root.left = previousNode
            previousNode = currentNode
            left = 0
            right = 1
        if right == 1:
            currentNode.value = lineWithoutSpaces[i]
            currentProblem.root.right = currentNode
            previousNode = currentNode
            left = 1
            right = 0
