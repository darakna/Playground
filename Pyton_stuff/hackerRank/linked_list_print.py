#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    print(head.data)
    if head.next:
        printLinkedList(head.next)


if __name__ == '__main__':
    #llist_count = int(input())
    llist_count = 4

    short_list = [22, 33, 44, 55]

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        #llist_item = int(input())
        llist_item = short_list[_]
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
