import unittest

from .generator import generate_random_elements
from .dataclass import RandomElements


class TestGenerateRandomElements(unittest.TestCase):
    def test_valid_input(self):
        input_list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']
        num_elements = 3
        result = generate_random_elements(input_list, num_elements)
        self.assertEqual(len(result.elements), num_elements)
        self.assertTrue(all(elem in input_list for elem in result.elements))
        self.assertIsInstance(result, RandomElements)

    def test_empty_list(self):
        input_list = []
        num_elements = 0
        result = generate_random_elements(input_list, num_elements)
        self.assertEqual(result.elements, [])
        self.assertIsInstance(result, RandomElements)

    def test_zero_elements(self):
        input_list = ['apple', 'banana', 'cherry']
        num_elements = 0
        result = generate_random_elements(input_list, num_elements)
        self.assertEqual(result.elements, [])
        self.assertIsInstance(result, RandomElements)

    def test_num_elements_equals_list_length(self):
        input_list = ['apple', 'banana', 'cherry']
        num_elements = 3
        result = generate_random_elements(input_list, num_elements)
        self.assertEqual(set(result.elements), set(input_list))
        self.assertIsInstance(result, RandomElements)

    def test_num_elements_greater_than_list_length(self):
        input_list = ['apple', 'banana', 'cherry']
        num_elements = 5
        with self.assertRaises(ValueError):
            generate_random_elements(input_list, num_elements)

    def test_input_list_with_duplicates(self):
        input_list = ['apple', 'apple', 'banana', 'cherry']
        num_elements = 2
        result = generate_random_elements(input_list, num_elements)
        self.assertEqual(len(result.elements), num_elements)
        self.assertTrue(all(elem in input_list for elem in result.elements))
        self.assertIsInstance(result, RandomElements)

    def test_str_representation(self):
        elements = RandomElements(['apple', 'banana'])
        self.assertEqual(str(elements), "['apple', 'banana']")

    def test_repr_representation(self):
        elements = RandomElements(['apple', 'banana'])
        self.assertEqual(repr(elements), "RandomElements(elements=['apple', 'banana'])")


if __name__ == "__main__":
    unittest.main()
