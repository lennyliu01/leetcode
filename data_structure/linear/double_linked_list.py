class Node:
    def __init__(self,data):
        self.data = data
        self.prior = None
        self.next = None
    def __repr__(self):
        return self.data


class doubleLinkedList:
    def __init__(self,nodes):
        self.head = None
        perv = None
        if nodes:
            curr = Node(nodes[0])
            curr.prior = perv
            perv = curr
            self.head = curr
            for node in nodes[1::]:
                curr = Node(node)
                curr.prior = perv
                perv.next = curr
                perv = curr


    def insert(self,index,data):
        if type(index) != int or index < 0:
            print("Error, the index has be a positive integer")
        i = 0
        node = Node(data)
        curr = self.head
        if index == 0:
            curr.prior = node
            node.next = curr
            self.head = node
    
        else:
            while curr:
                if i == index-1:
                    if curr.next != None:
                        next = curr.next
                        curr.next = node
                        node.prior = curr
                        node.next = next
                        next.prior = node
                        return
                    else:
                        curr.next = node
                        node.prior = curr
                        return
                else:
                    i += 1
                    curr = curr.next
            print(f"index is out of bound, the list's max insert index is {i}, the insert postion is {index}")

    def __repr__(self):
        dot = self.head
        dots = []
        while dot is not None:
            dots.append(dot.data)
            dot = dot.next
        return ' -> '.join(dots) + ' reverse: ' + ' -> '.join(dots[::-1])

dlist = doubleLinkedList(['a','b'])
print(dlist)
dlist.insert(3,'1')
print(dlist)