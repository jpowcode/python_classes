"""
Start using the unittest library to run tests. Each set of sets will be defined
as a class. Each class will have a method to set up what it needs to perform
the tests. For example, a populated array. We are testing that we cannot enter
incorrect data types or an incorrect array size. The version number on this file
matches the version number on the myarray file. From now on as we add more
functionality to the array class we will add more tests to the test file.
"""

import unittest
from myarray_3 import MyArray


class TestArrayInput(unittest.TestCase):

    def setUp(self):
        self.my_empty_array = MyArray(3, 'int8')
        self.my_full_array = MyArray(3, 'int8')
        self.my_full_array.input([3 ,2, 1])

    def test_incorrect_data_char(self):
        self.assertEqual(self.my_empty_array.input(['a',2, 1]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_float(self):
        self.assertEqual(self.my_empty_array.input([3.2, 2, 1]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_big(self):
        self.assertEqual(self.my_empty_array.input([3.2, 2, 300]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_negative(self):
        self.assertEqual(self.my_empty_array.input([3, -2, 1]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_edge(self):
        self.assertEqual(self.my_empty_array.input([0, -2, 1]), 'Incorrect data type', "Should be Incorrect data type")

    def test_incorrect_data_size(self):
        self.assertEqual(self.my_empty_array.input([5, -2, 1, 4]), 'Incorrect data size', "Should be Incorrect data size")

    def test_incorrect_data_correct(self):
        self.assertEqual(self.my_full_array.array, [3, 2, 1] , "Should be [3, 2, 1]")


if __name__ == '__main__':
    unittest.main()