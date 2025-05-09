# this is where we will test the link
from TestLinkedList import TestLinkedList
test1 = TestLinkedList()

test1.addNode(10)
test1.addNode(20)
test1.addNode(25)
test1.addNode(34)

print("Before removing:")
test1.show()

test1.Remove_Node(25)

print("After removing 25: ")
test1.show()

test1.insertingNode_at(0,55)
print("After inserting 55: ")
test1.show()

