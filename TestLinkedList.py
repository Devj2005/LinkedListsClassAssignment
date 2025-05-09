# This file is used to define the logic of a linked-list
from Node import Node


class TestLinkedList:
    def __init__(self):
        self.start = None # This is used to point to the first node on the lisy

    def addNode(self,val): #This is used to add a new node to the end of the list
        New_Node = Node(val)
        if self.start is None:
            self.start = New_Node # If the list is empty, new node becomes the first node in the list
            return

        temp = self.start #otherwise move to the end and link the new node to the list
        while temp.link:
            temp = temp.link
        temp.link = New_Node



    def insertingNode_at(self, posi , val):
        New_Node = Node(val)
        if posi == 0:
            New_Node.link = self.start #inserts node at the beginning
            self.start = New_Node

            return

        temp = self.start


        for _ in range(posi - 1): # traverse to the node before the insertion point
            if temp is None:
                print("Position  is out of range")
                return
            temp = temp.link

        if temp is None:
            print("Position is out  of range!!")
            return

        New_Node.link = temp.link #Insert the node by adjusting the pointers
        temp.link = New_Node


    def Remove_Node (self, val): # it removes the first node that contains a given value.
        temp = self.start
        prev = None
        while temp:
            if temp.val == val:
                if prev: #it is not the first node

                    prev.link = temp.link
                else:# node is the first one
                    self.start = temp.link
                return
            prev = temp
            temp = temp.link

        #Display the entire list
    def show(self):
            temp = self.start
            while temp:
                print(temp.val, end=" --->")
                temp = temp.link

            print("None!!") #this shows the end of the list


