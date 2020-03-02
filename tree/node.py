class Node:
    id = 0
    parent = ''
    left = ''
    right = ''
    operation = ''

    def __init__(self, left, right, n_id):
        self.left = left
        self.right = right
        self.id = n_id

    def add_parent(self, parent):
        self.parent = parent

    def add_operation(self, operation):
        self.operation = operation

    def p_node(self):
        print("L: " + str(self.left) + " R: " + str(self.right))
        print("OP: ", self.operation)