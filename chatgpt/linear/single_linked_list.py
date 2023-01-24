class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current:
            if count == position - 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            count += 1
