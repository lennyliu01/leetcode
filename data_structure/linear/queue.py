'''A Queue is a FIFO  (first in, first out) list with the following opera:ons: Enqueue, Dequeue, Size, Font.'''


class Queue():
    def __init__(self):
        '''Queue () creates a new queue that is empty. It needs no parameters and returns an empty queue. '''
        self.items = []
        self.s = 0


    def isEmpty(self):
        '''isEmpty () tests to see whether the queue is empty. It needs no parameters and returns a boolean value. '''
        return True if self.items == [] else False


    def enqueue(self,item):
        '''Enqueue (item) adds a new item to the rear of the queue. It needs the item and returns nothing. '''
        self.items.append(item)
        self.s += 1


    def dequeue(self):
        '''equeue () removes the item from the front of the queue. It needs no parameters and returns the item. The queue is modified. '''
        if self.isEmpty():
            return 'The queue is empty, no action taken'
        else:
            self.s -= 1
            return self.items.remove(0)


    def front(self):
        '''Front () returns the front item from the queue but does not remove it. It needs no parameters. The queue is not modified. '''
        if self.isEmpty():
            return('The queue is empty')
        else:
            return self.items[0]


    def size(self):
        '''size () returns the number of items on the queue. It needs no parameters and returns an integer. '''
        return self.s

    
    def delete(self):
        '''Remove the queue from the momery, It needs no parameters and no returns '''
        del self.items
    
    
    def clear_queue(self):
        '''empty the queue, It needs no parameters and no returns '''
        self.items = []


    def get(self,val):
        i = 0
        for item in self.items:
            if item == val:
                return i
            else:
                i += 1
        return f'{val} not found in the queue'