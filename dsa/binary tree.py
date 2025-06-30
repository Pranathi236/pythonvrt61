class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def _init_(self):
        self.root=None
    def insert(self,data):
        new_node=Node(data)
        if not self.root:
            self.root=new_node
            return
        queue=[self.root]
        while queue:
            temp=queue.pop(0)
            if not temp.left:
                temp.left=new_node
                return
            else:
                queue.append(temp.left)
            if not temp.right:
                temp.right=new_node
                return
            else:
                queue.append(temp.right)
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=' ')
            self.inorder(node.right)
    def preorder(self,node):
        if node:
            print(node.data,end=' ')
            self.preorder(node.left)
            self.preorder(node.right)
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data,end=' ')
    def level_order(self):
        if not self.root:
            return
        queue=[self.root]
        while queue:
            temp=queue.pop(0)
            print(temp.data, end=' ')
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
bt=BinaryTree()
for val in [10,5,15,3,7,12,18]:
    bt.insert(val)
print("Inorder:")
bt.inorder(bt.root)
print("\npreorder:")
bt.preorder(bt.root)
print("\npostorder:")
bt.postorder(bt.root)
print("\nlevel order:")
bt.level_order()         
