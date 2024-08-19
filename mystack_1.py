"""
Create a Stack structure that inherits from an Array. We need to run the
constructor for the Array. Relabel the size of the array as max_size and set the
current size of the stck to be -1 for empty. The stack will not always take up
the full size of the array. We add an atribute called structure that tells us
we are dealing with a stack. This will be useful in future when we inherit from
the Stack class to create a Queue.
"""

from myarray_5 import MyArray

class MyStack(MyArray):
    def __init__(self, max_size, stack_type):
        MyArray.__init__(self, max_size, stack_type)
        self.stack_size = -1
        self.max_size = self.i
        self.structure = "stack"



