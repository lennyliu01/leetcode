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
    

    def top(self):
        '''top() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.'''
        return self.items[-1]

    
    def size(self):
        '''size() returns the number of items on the stack. It needs no parameters and returns an integer.'''
        return self.s
