"""
Add a helper method called check_type to check a value is of the correct type.
For example to check a number is an integer between 0 and 255. This method will
be used later when we add values to the array. A few tests have been added below.
"""

class MyArray:
    def __init__(self, i, array_type):
        """Allowed types
             - int8: 8 bit signed integer 0 - 2^8 -1
             - char: a single character
        """
        self.array = []
        self.i = i
        self.array_type = array_type

        for _ in range(self.i):
            self.array.append(None)

    def check_type(self, value):
        if self.array_type == 'int8':
            return isinstance(value ,int) and 0 < value <= 255

        elif self.array_type == 'char':
            return isinstance(value, str) and len(value) == 1



print("""
Conduct Tests
________________________________________________________________________

""")

print("Check we can create a class, there should be no errors")
array_1 = MyArray(1,'int8')
array_2 = MyArray(1,'char')

print("Check the check_type function works correctly")
print(array_1.check_type(1))
print(array_1.check_type(0.5))
print(array_1.check_type(280))
print(array_1.check_type(255))
print(array_1.check_type(0))

print(array_2.check_type("a"))
print(array_2.check_type(0.5))
print(array_2.check_type("hello"))
