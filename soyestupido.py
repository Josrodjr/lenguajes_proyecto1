
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