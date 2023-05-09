# Implementation of a Binary Tree Data Structure
class TreeNode:

    def __init__(self):
        self.right = None
        self.left = None
        self.value = None

    def setRight(self, right):
        self.right = right

    def setLeft(self, left):
        self.left = left

# Implementation of a Binary Search Tree Data Structure
class BST:

    def __init__(self):
        self.root = None 

    def insertRecursive(self, rootNode, node):
        
        if node.value < rootNode.value and rootNode.left == None:
            rootNode.setLeft(node)
            return None

        if node.value > rootNode.value and rootNode.right == None:
            rootNode.setRight(node)
            return None

        if node.value < rootNode.value:
            rootNode = rootNode.left
        elif node.value > rootNode.value:
            rootNode = rootNode.right

        self.insertRecursive(rootNode, node)


    def insert(self, node):
        
        if self.root == None:
            self.root = node 
        else:
            self.insertRecursive(self.root, node)