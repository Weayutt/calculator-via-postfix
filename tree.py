#Author: Wyatt Avilla
#Date: 11/12/22
#File: Contains tree classes
#implementation from https://runestone.academy/ns/books/published/pythonds/index.html

from stack import Stack
class BinaryTree:

    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    def __str__(self):
        L = self.getLeftChild()
        R = self.getRightChild()
        if self.getLeftChild() == None:
            L = ""
        if self.getRightChild() == None:
            R = ""
        return (f"{self.key}({L})({R})")

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        if self.leftChild == None:
            return(None)
        else:
            return self.leftChild

    def getRightChild(self):
        if self.rightChild == None:
            return(None)
        else:
            return self.rightChild

    def getRootVal(self):
        return str(self.key)

    def setRootVal(self, rootObj):
        self.key = rootObj


class ExpTree (BinaryTree):
    
    def make_tree(postfix):
        true_opers = ["*", "/", "+", "-", "^"]
        s = Stack()
        for x in postfix:
            if x in true_opers:              # adds node containing numerical value to stack
                R = s.pop()
                L = s.pop()
                new_expr_tree = ExpTree(x)
                new_expr_tree.leftChild = (L)
                new_expr_tree.rightChild = (R)
                s.push(new_expr_tree)
            else:                            # adds expression tree to stack
                new_tree = ExpTree(x)  
                s.push(new_tree)
        return(s.pop())
        
    def __str__(self):
        return ExpTree.inorder(self)

    def preorder(tree):
        s = ""
        if tree != None:
            s = tree.getRootVal()
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
        return s

    def postorder(tree):
        s = ""
        if tree != None:
            s += ExpTree.postorder(tree.getLeftChild())
            s += ExpTree.postorder(tree.getRightChild())
            s += tree.getRootVal()
        return s
    
    def inorder(tree):
        s = ""
        if tree != None:
            if tree.getLeftChild() != None and tree.getRightChild != None:
                s += (f"({ExpTree.inorder(tree.getLeftChild())}")
                s += (f"{tree.getRootVal()}")
                s += (f"{ExpTree.inorder(tree.getRightChild())})")
            else:
                s += (f"{ExpTree.inorder(tree.getLeftChild())}")
                s += (f"{tree.getRootVal()}")
                s += (f"{ExpTree.inorder(tree.getRightChild())}")
        return s
    
    def evaluate(tree):
        if tree.getRootVal == None:                                      # base case 1
            return 0
        if tree.getLeftChild() == None and tree.getRightChild() == None: # base case 2
            return float(tree.getRootVal())
        
        leftval = (ExpTree.evaluate(tree.getLeftChild()))
        rightval = (ExpTree.evaluate(tree.getRightChild()))

        if tree.getRootVal() == "*":
            return leftval * rightval
        if tree.getRootVal() == "/":
            return leftval / rightval
        if tree.getRootVal() == "+":
            return leftval + rightval
        if tree.getRootVal() == "-":
            return leftval - rightval
        if tree.getRootVal() == "^":
            return leftval**rightval

    