"""
We add methods for push, pop and top. Push should put a value on to the top of
the stack. Pop should remove a value from the top of the stack and return it.
Top should return the value from the top of the stack without removing it.

"""

from myarray_5 import MyArray

class MyStack(MyArray):
    def __init__(self, max_size, stack_type):
        MyArray.__init__(self, max_size, stack_type)
        self.stack_size = -1
        self.max_size = self.i

    def height(self):
        return self.stack_size + 1

    def isEmpty(self):
        return self.stack_size < 0

    def push(self, value):
        if self.stack_size + 1 == self.max_size:
            return(self.structure, 'is full')
        else:
            self.stack_size += 1
            self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            return(self.structure, 'is empty')
        else:
            temp = self.stack[self.stack_size]
            del self.stack[-1]
            self.stack_size -=1
            return temp

    def top(self):
        if self.isEmpty():
            return(self.structure, 'is empty')
        else:
            return self.stack[-1]