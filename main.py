import copy

from libs.parser import parse_input
from tree.node import Node
from builder import create_node, name_parents

# try the print of the tree
from libs.print_tree import print2D

# get the array of parsed data
operations = parse_input('(a|b)* a b')

# construct the tree based on the highest priority on the first level first
tree = create_node(operations)

# travel tree top down to assign parent to children
name_parents(tree, 'root')

# print the final state of the tree
print2D(tree)

# print(tree.parent)
# print(tree)
# print(tree.right.parent)
# print(tree.left.parent)
# print(tree.right.right.parent)
# print(tree.right.right.right)
# print(tree.right.right.operation)
# print(tree.right.right.left)
