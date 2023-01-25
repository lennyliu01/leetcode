class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    
    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self,nodes=None):
        self.head = None
        if nodes:
            self.head = Node(nodes.pop(0))
            p = self.head
            for node in nodes:
                p.next = Node(data=node)
                p = p.next

    
    def insert(self, index, data):
        if type(index)!= int:
            return "Error, the index has be an interge"
        i = 0
        node = Node(data)
        p = self.head
        if index == 0:
            node.next = p
            self.head = node
        else:
            while p:
                if i == index-1: #if index = 3, get the element at index 2
                    node.next = p.next
                    p.next = node
                    return
                i += 1
                p = p.next
        if i < index:
            print(f"index is out of bound, the list's max insert index is {i}, the insert postion is {index}")


    def remove(self,index=None):
        if type(index)!= int:
            return "Error, the index has be an interge"
        i = 0
        p = self.head
        if index == 0:
            q = p.next
            self.head = q
            p.next = None
            return
        try:
            while p:
                if i == index-1:
                    q = p.next
                    p.next = q.next
                    q.next = None
                    return 
                else:
                    i += 1
                    p = p.next
        except:
            print(f"Error, index {index} is out of range, the max index for this list is {i}")
    

    def get_by_index(self,index):
        if type(index) != int or index <0:
            print("index has be to an positive interge, existing")
        else:
            p = self.head
            i = 0
            while p:
                if i == index:
                    return p
                else:
                    i += 1
                    p = p.next
            return(f'The index {index} is out of range, the max index for this list is {i-1}')
            #return -1

    def get_by_value(self,data):
        if data:
            p = self.head
            i = 0
            while p:
                if p.data == data:
                    return i
                else:
                    p = p.next
                    i += 1
        return (f'{data} is not found in the linked list')


    def __repr__(self):
        dot = self.head
        dots = []
        while dot is not None:
            dots.append(dot.data)
            dot = dot.next
        return ' -> '.join(dots)



llist = LinkedList(['a','b','c'])
# first_node = Node('a')
# second_node = Node('b')
# third_node = Node('c')
# first_node.next = second_node
# second_node.next = third_node
# llist = LinkedList()
# llist.head = first_node
print(llist)
llist.insert(3,'1')
print(llist)
# print(llist.get_by_index(1))
# print(llist.get_by_value('1'))
llist.remove(3)
print(llist)