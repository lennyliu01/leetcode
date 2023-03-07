import unittest
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    
    def __repr__(self):
        return str(self.data)

#头插法
class LinkedList:
    def __init__(self,nodes=None):
        self.head = None
        perv = None
        while nodes:
            current = Node(nodes.pop())
            current.next = perv
            perv = current
        self.head = perv

# 尾插法
# class LinkedList:
#     def __init__(self,nodes=None):
#         self.head = None
#         if nodes:
#             p = Node(nodes.pop(0))
#             self.head = p
#             for n in nodes:
#                 p.next = Node(n)
#                 p = p.next

    def __repr__(self):
        dot = self.head
        dots = []
        while dot is not None:
            dots.append(str(dot.data))
            dot = dot.next
        return ' -> '.join(dots)
    
    
    # def merge(self,l1, l2):
    #     dummy = Node(0)
    #     tail = dummy
    #     while l1 and l2:
    #         if l1.head.data < l2.head.data:
    #             tail.next = l1
    #             l1.head = l1.next
    #         else:
    #             tail.next = l2
    #             l2.head = l2.next
    #         tail = tail.next
    #     tail.next = l1 if l1 else l2
    #     return dummy.next
        
# def merge(node1,node2):
#     dummy = Node(0) #存储其实指针
#     tail = dummy
#     while node1 and node2 != None:
#         if node1.data <= node2.data:
#             tail.next = node1
#             node1 = node1.next
#         else:
#             tail.next = node2
#             node2 = node2.next
#         tail = tail.next
#     if node1:
#         tail.next = node1
#     else:
#         tail.next = node2
#     return dummy.next

def merge(n1,n2):
    dummy = Node(1)
    tail = dummy
    while n1 and n2:
        if n1.data > n2.data:
            tail.next = n2
            n2 = n2.next
        else:
            tail.next = n1
            n1 = n1.next
        tail = tail.next
    tail.next = n1 if n1 else n2
    return dummy.next




# l1= LinkedList([1,7,8])
# l2 = LinkedList([1,2,4,5,6,10,12])
l1=LinkedList([[1,1],[-5,2],[3,4]])
l2=LinkedList([[1,1],[4,2],[3,4],[2,8],[1,10]])
print(l1)
print(l2)
#l1 = LinkedList()
#l2 = LinkedList(0)
# node_1 = l1.head
# node_2 = l2.head

#node3 = merge(node_1, node_2)
# print(node3.next.next.next)
#l3 = LinkedList()
#l3.head = node3
#print(l3)


class TestLinkedList(unittest.TestCase):
    def test_init_with_nodes(self):
        linked_list = LinkedList([1, 2, 3])
        self.assertEqual(linked_list.head.data, 1)
        self.assertEqual(linked_list.head.next.data, 2)
        self.assertEqual(linked_list.head.next.next.data, 3)
        self.assertIsNone(linked_list.head.next.next.next)
        
    def test_init_without_nodes(self):
        linked_list = LinkedList()
        self.assertIsNone(linked_list.head)

if __name__ == '__main__':
    unittest.main()


