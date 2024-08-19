"""
We add some magic methods to allow stacks to perform as normal data structures
in python. For example if we create two stacks S1 and S2 that are the same and
ask python S1 == S2 then we should get the reult True. This is performed by the
__eq__ method. If we perform str(S1) then __str will deal with this.

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


    def __str__(self):
        output = [str(x) for x in self.stack]
        return ','.join(output)


    def __eq__(self, other):
        if self.max_size != other.max_size:
            return False

        for i, j in zip(self.stack, other.stack):
            if i != j:
                return False
        return True


