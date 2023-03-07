import unittest

'''A stack is a LIFO (last in, first out) list with the following operation: (Push, Pop, Create  Init), 
Top, IsEmpty, Size.  Such a list is called a Signature or the Interface to the ADT.'''

class Stack():
    def __init__(self):
        self.items = []
        self.s = 0

    
    def __repr__(self):
        return str(self.items)


    def isEmpty(self):
        '''isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.'''
        return True if self.items == [] else False

    
    def push(self,item):
        '''push(item) adds anew item to the top of the stack.  It needs the item and returns nothing'''
        self.items.append(item)
        self.s += 1


    def pop(self):
        '''pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.'''
        item = self.items.pop()
        self.s -= 1
        return item
    

    def peek(self):
        '''top() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.'''
        return self.items[-1]

    
    def size(self):
        '''size() returns the number of items on the stack. It needs no parameters and returns an integer.'''
        return self.s

    
    # def delete(self):
    #     '''Remove the stack from the momery, It needs no parameters and no returns '''
    #     del self.items
    
    
    def clear_stack(self):
        '''empty the stack, It needs no parameters and no returns '''
        self.items = []

# The method get(self, val) is not part of the stack's standard LIFO operations
    # def get(self,val):
    #     i = 0
    #     for item in self.items:
    #         if item == val:
    #             return i
    #         else:
    #             i += 1
    #     return f'{val} not found in the stack'


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_is_empty(self):
        self.assertTrue(self.stack.isEmpty())
        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty())
        
    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.isEmpty())
    
    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.peek(), 1)
    
    def test_size(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 3)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 2)
    
    def test_clear_stack(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.clear_stack()
        self.assertTrue(self.stack.isEmpty())

if __name__ == '__main__':
    unittest.main()