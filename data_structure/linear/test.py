class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    
    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self,nodes=None):
        self.head = None
        # perv = None
        # while nodes:
        #     current = Node(nodes.pop())
        #     current.next = perv
        #     perv = current
        # self.head = perv
        if nodes:
            p = Node(nodes.pop(0))
            self.head = p
            for n in nodes:
                p.next = Node(n)
                p = p.next


    def __repr__(self):
        dot = self.head
        dots = []
        while dot is not None:
            dots.append(dot.data)
            dot = dot.next
        return ' -> '.join(dots)



llist = LinkedList(['a','b','c','d'])
print(llist)