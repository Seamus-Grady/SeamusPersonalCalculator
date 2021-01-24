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
    for i in range(0, len(lineWithoutSpaces)):
        currentNode = node()
        if i == 0:
            currentNode.value = lineWithoutSpaces[i]
            currentProblem.root = currentNode
            previousNode = currentNode
            left = 1
        elif left == 1:
            currentNode.value = lineWithoutSpaces[i]
            currentProblem.root = currentNode
            currentProblem.root.left = previousNode
            previousNode = currentNode
            left = 0
            right = 1
        elif right == 1:
            currentNode.value = lineWithoutSpaces[i]
            currentProblem.root.right = currentNode
            left = 1
            right = 0
    return currentProblem
def solveTheTree(tree):
    if tree is None:
        return
    left = solveTheTree(tree.left)
    right = solveTheTree(tree.right)
    if left is None and right is None:
        return int(tree.value)
    elif type(left) != int or type(right) != int:
        raise Exception()
    elif tree.value == '+':
        return left + right
    elif tree.value == '*':
        return left * right
    elif tree.value == '/':
        if right == 0:
            raise Exception()
        else:
            return left / right
    elif tree.value == '-':
        return left - right

for line in sys.stdin:
    try:
        print(solveTheTree(buildTheTree(line.rstrip()).root))
    except:
        print('Error')
