class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, index, data):
        if type(index)!= int:
            return "Error, the index has be an interge"
        else:
            node = Node(data)
            p = self.head
            i = 0
            if index == 0:
                node.next = p
                self.head = node
            else:
                while p:
                    if i == index-1: #if index = 3, get the element at index 2
                        node.next = p.next
                        p.next = node
                        return 
                    else:
                        i += 1
                        p = p.next
            #print(f"index is out of bound, the list's max index is {i-1}, the insert postion is {index}")
    def __repr__(self):
        dot = self.head
        dots = []
        while dot is not None:
            dots.append(dot.data)
            dot = dot.next
        return ' -> '.join(dots)

llist = LinkedList()
first_node = Node('a')
second_node = Node('b')
third_node = Node('d')
llist.head = first_node
first_node.next = second_node
second_node.next = third_node
print(llist)
llist.insert(2,'c')
print(llist)
