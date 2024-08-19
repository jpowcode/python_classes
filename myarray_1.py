"""
Create the MyArray class with a constructor method. At the moment this is a
one dimensional array. The class takes as input a number i for the size of the
array and a string that specifies the type as either an integer or a character.
The constructor metho sets the variables i and array_type and also creates an
empty list to hold the array elemnets. The array is then populated with None
values. We test there are no errors by creating an instance of the array.
"""

class MyArray:
    def __init__(self, i, array_type):
        """Allowed types
             - int8: 8 bit unsigned integer 0 - 2^8 -1
             - char: a single character
        """
        self.__array = []
        self.i = i
        self.array_type = array_type

        for _ in range(i):
            self.__array.append(None)


array_1 = MyArray(1, 'char')
print(array_1.__array)
array_1.array = 5
#print(array_1.array)