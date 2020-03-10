import copy

from libs.parser import parse_input
from tree.node import Node

# construct the tree based on the highest priority on the first level first

operators = ' |*+?'

precedence = {
    ' ': 0,
    '|': 0,
    '*': 2,
    '+': 1,
    '?': 0
}
# not isinstance(operation_array[0], Node) or

op_type = {
    ' ': 'bin',
    '|': 'bin',
    '*': 'un',
    '+': 'un',
    '?': 'un'
}

def create_node(operation_array):
    # construct of this node
    # created_node = Node(0,0,0)
    
    while len(operation_array) > 1:

        # run the entire list eliminating parenthesis
        for i in range(len(operation_array)):
            if isinstance(operation_array[i], list):
                new_node = create_node(operation_array[i])
                operation_array[i] = new_node
                # print(operation_array)
        
        # if everything is on the same level (no parenthesis exist)
        ocurrences = 0
        for value in operation_array:
            if isinstance(value, list):
                ocurrences += 1

        # nth loop after everything is either node or same level
        if ocurrences == 0:
            current_ops = []
            # get all the operands in this level
            for i in range(len(operation_array)):
                if not isinstance(operation_array[i], Node):
                    if operation_array[i] in operators:
                        current_ops.append([operation_array[i], i])

            # select the hightest precedence one and build the tree from it
            highest = current_ops[0]
            for value in current_ops:
                if precedence[value[0]] >= precedence[highest[0]]:
                    highest = value

            # check if its bin or un
            curr_type = op_type[highest[0]]

            if curr_type == 'bin':
                # get next and previous value and build node
                l_value = copy.deepcopy(operation_array[highest[1]-1])
                r_value = copy.deepcopy(operation_array[highest[1]+1])

                # pop from original array the values of both operands and the operator
                operation_array.pop(highest[1]+1)
                operation_array.pop(highest[1])
                operation_array.pop(highest[1]-1)


                node = Node(l_value, r_value, 0)
                node.add_operation(highest[0])

                operation_array.append(node)
                # print(operation_array)


            if curr_type == 'un':
                # get previous vaue and build node
                r_value = operation_array[highest[1]-1]

                operation_array.pop(highest[1])
                operation_array.pop(highest[1]-1)

                node = Node(0, r_value, 0)
                node.add_operation(highest[0])

                operation_array.append(node)

                # print(operation_array[0])

    return operation_array[0]                                                                                                                                                                                                                                                                    