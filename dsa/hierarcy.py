class Employee:
    def __init__(self, name):
        self.name = name
        self.left = None  # Left subordinate
        self.right = None  # Right subordinate

# Sample hierarchy setup
ceo = Employee("CEO")
cto = Employee("CTO")
cfo = Employee("CFO")
dev1 = Employee("Dev1")
dev2 = Employee("Dev2")
acc1 = Employee("Acc1")
acc2 = Employee("Acc2")

ceo.left = cto
ceo.right = cfo
cto.left = dev1
cto.right = dev2
cfo.left = acc1
cfo.right = acc2

# Traversals
def in_order(node):
    if node:
        in_order(node.left)
        print(node.name, end=' ')
        in_order(node.right)

def pre_order(node):
    if node:
        print(node.name, end=' ')
        pre_order(node.left)
        pre_order(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.name, end=' ')

# Count leaf nodes
def count_leaves(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

# Calculate tree height
def tree_height(node):
    if not node:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

# Find manager of a given employee
def find_manager(root, target_name, manager=None):
    if not root:
        return None
    if root.name == target_name:
        return manager
    left = find_manager(root.left, target_name, root.name)
    if left:
        return left
    return find_manager(root.right, target_name, root.name)

# Demo run
print("In-Order Traversal:")
in_order(ceo)

print("\nPre-Order Traversal:")
pre_order(ceo)

print("\nPost-Order Traversal:")
post_order(ceo)

print("\n\nTotal Leaf Employees:", count_leaves(ceo))
print("Hierarchy Depth:", tree_height(ceo))
print("Manager of Acc2:", find_manager(ceo, "Acc2"))