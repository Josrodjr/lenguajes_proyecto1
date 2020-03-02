from node import Node

testnode = Node(1,2,0)
testnode.add_operation('|')
tnode2 = Node(testnode, None, 1)
tnode2.add_operation('*')



testnode.p_node()
tnode2.p_node()
