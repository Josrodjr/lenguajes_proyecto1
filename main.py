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

# graficadora(tree.automata['transitions'], tree.automata['start_end'])


# hacer la simulacion del automata para una cadena de strings

def e_closure(automata, state):
    transitions = automata['transitions']
    reachable_states = set()
    # iterate over the transitions searching for reachable states of first state
    for transition in transitions:
        if transition[0] == state:
            if transition[1] == 0:
                reachable_states.add(transition[2])

    # iterate over the found reachable states until something changes
    return reachable_states


def get_eclosure(tree, init_state):
    e1 = set()
    e2 = set()
    e1.add(init_state)

    while e2 != e1:
        e2 = copy.deepcopy(e1)
        t_set = copy.deepcopy(e1)
        for value in e1:
            new = e_closure(tree.automata, value)
            for result in new:
                t_set.add(result)
        e1 = copy.deepcopy(t_set)
    
    return e1


init_state = tree.automata['start_end'][0][0]

print(get_eclosure(tree, init_state))


# print(e_closure(tree.automata, init_state))