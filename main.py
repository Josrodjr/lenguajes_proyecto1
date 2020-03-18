import copy

from libs.parser import parse_input, remove_empty
from tree.node import Node
from builder import create_node, name_parents, create_automata_last, create_automata
from tree.utils import FindDeepestNode


# try the print of the tree
from libs.print_tree import print2D
# try and print the nodes
from libs.grafo import graficadora
# get non_det functions
from finite_automata.automata import automata_template, create_or, create_and, create_kleene, create_plus, create_qmark

# get the array of parsed data
operations = parse_input('(a|ε) b (a+) c?')
# operations = parse_input('(a*|b*) c')
operations = remove_empty(operations)

print(operations)

# construct the tree based on the highest priority on the first level first
tree = create_node(operations)

# travel tree top down to assign parent to children
name_parents(tree, 'root')

# print the final state of the tree
print2D(tree)

# find the node we start building from
o = FindDeepestNode()
first = o.deepest_node(tree)


def fill_tree(tree):
    # do bottom one time
    create_automata_last(tree)
    while len(tree.automata) == 0:
        # do leaves one by one from bottom
        create_automata(tree)

fill_tree(tree)
print(tree.automata)

graficadora(tree.automata['transitions'], tree.automata['start_end'])

