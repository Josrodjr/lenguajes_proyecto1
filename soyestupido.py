
def build_node(operation_array):

     

    while True:
        if len(operation_array) == 0:
            break

        current_ops = []
        # get all the operands in this level
        for i in range(len(operation_array)):
            if not isinstance(operation_array[i], list):
                if operation_array[i] in operators:
                    current_ops.append([operation_array[i], i])

        # select the hightest precedence one and build the tree from it
        highest = current_ops[0]
        for value in current_ops:
            if precedence[value[0]] >= precedence[highest[0]]:
                highest = value

        # start building the tree based on the highest precedence op
        # check if its bin or un
        curr_type = op_type[highest[0]]

        if curr_type == 'bin':
            # get next and previous value and build node
            l_value = operation_array[highest[1]-1]
            r_value = operation_array[highest[1]+1]

            # pop from original array the values of both operands and the operator
            operation_array.pop(highest[1]-1)
            operation_array.pop(highest[1]+1)
            operation_array.pop(highest[1])

            # if both ends not array
            if not isinstance(r_value, list):
                if not isinstance(l_value, list):
                    node = Node(l_value, r_value, 0)
                    node.add_operation(highest[0])
                    return node
                else:
                    l_value = build_node(l_value)
                    node = Node(l_value, r_value, 0)
                    node.add_operation(highest[0])
                    return node

        if curr_type == 'un':
            # get previous vaue and build node
            l_value = operation_array[highest[1]-1]

            operation_array.pop(highest[1]-1)
            operation_array.pop(highest[1])

            if not isinstance(l_value, list):
                node = Node(l_value, 0, 0)
                node.add_operation(highest[0])
                return node
            else:
                l_value = build_node(l_value)
                node = Node(l_value, 0, 0)
                node.add_operation(highest[0])
                return node

        print(operation_array)

build_node(operations)





# or
current_state_numerator = 7
start_end = [[1, 1], [7, 7]]
transitions = [[1, 0, 2],[2, 0, 3], [2, 0, 5], [3, 'VAL1', 4], [5, 'VAL2', 6], [4,0,7], [6,0,7]]

operators = ['a', 'b']

for transition in transitions:
    if transition[1] != 0:
        transition[1] =  operators.pop()



# agregar un or dentnro de un or test
start_end1 = [[1, 1], [7, 7]]
transitions1 = [[1, 0, 2],[2, 0, 3], [2, 0, 5], [3, 'VAL1', 4], [5, 0, 6], [4,0,7], [6,0,7]]

# change the numerator of each interation
for state in start_end1:
    state[0] += current_state_numerator
    state[1] += current_state_numerator

for transition in transitions1:
    transition[0] += current_state_numerator
    transition[2] += current_state_numerator

for transition in transitions1:
    if transition[1] != 0:
        # add kleene operation from base node to start
        transition[1] = 0
        transition[2] = start_end[0][0]
        # add end node to operations
        transitions1.append([start_end[1][0], 0, transition[2]])

transitions = transitions + transitions1


# start at the deepest node found building the tree
# def build_NFA(tree, current_node, current_nfa):
#     if tree == current_node:
#         # do one last operation and return the finished NFA
#         # check if node type
#         left_op = current_node.left
#         right_op = current_node.right
#         if isinstance(left_op, Node):
#             # if there is no automata formed until now
#             if len(left_op.automata) == 0:
#                 # throw build_NFA from this point
#                 left_op.automata = build_NFA(left_op) 


#         if current_node.operation == '|':
            
#     else:
#         # do operation and continue climbing
