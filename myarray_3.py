"""
In order to populate our arrays we need an input method. This method takes as
a paraeter a list of values. It fist checks whether the length of this list is
the correct length for the array. It then checks that the type of each value
in the list is correct for the type of the array. If both of these are true then
it will populate the array. I have not included any tests at the the end of this
file. They will be included i the next iteration.
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
            return isinstance(value ,int) and 0 < value < 255

        elif self.array_type == 'char':
            return isinstance(value, str) and len(value) == 1

    def input(self, values):
        if len(values) != self.i:
            return 'Incorrect data size'

        for value in values:
            if not self.check_type(value):
                return 'Incorrect data type'

        for index in range(self.i):
            self.array[index] = values[index]