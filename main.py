import copy

from libs.parser import parse_input
from tree.node import Node
from builder import create_node

# try the print of the tree
from libs.print_tree import print2D


# get the array of parsed data
operations = parse_input('(a|b)* a b')

# construct the tree based on the highest priority on the first level first

tree = create_node(operations)

# tree.right.p_node()
# tree.right.right.p_node()

# travel tree top down to assign parent to children

def name_parents(tree, count):
    tree.id = count
    count += 1
    if isinstance(tree.left, Node):
        # repeat this same method for the left side
        name_parents(tree.left, count)
        
    if isinstance(tree.right, Node):
        # repeat this same method for the right side
        name_parents(tree.right, count)


name_parents(tree, 1)

print2D(tree)
