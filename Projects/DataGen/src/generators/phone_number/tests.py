import unittest

from .generator import generate_phone_numbers
from .dataclass import PhoneNumber


class TestGeneratePhoneNumbers(unittest.TestCase):
    def test_single_number_default_length(self):
        numbers = generate_phone_numbers(1)
        self.assertEqual(len(numbers), 1)
        self.assertTrue(all(len(num.number) == 10 for num in numbers))
        self.assertTrue(all(isinstance(num, PhoneNumber) for num in numbers))

    def test_multiple_numbers(self):
        numbers = generate_phone_numbers(44, 5)
        self.assertEqual(len(numbers), 5)
        self.assertTrue(all(len(num.number) == 10 for num in numbers))
        self.assertTrue(all(isinstance(num, PhoneNumber) for num in numbers))

    def test_full_number(self):
        phone_number = PhoneNumber(1, '1234567890')
        self.assertEqual(phone_number.full_number, '+11234567890')

    def test_str_representation(self):
        phone_number = PhoneNumber(1, '1234567890')
        self.assertEqual(str(phone_number), '+11234567890')

    def test_repr_representation(self):
        phone_number = PhoneNumber(1, '1234567890')
        self.assertEqual(repr(phone_number), "PhoneNumber(country_code=1, number='1234567890')")

    def test_custom_length(self):
        numbers = generate_phone_numbers(91, 3, 8)
        self.assertEqual(len(numbers), 3)
        self.assertTrue(all(len(num.number) == 8 for num in numbers))
        self.assertTrue(all(isinstance(num, PhoneNumber) for num in numbers))

    def test_invalid_country_code(self):
        with self.assertRaises(ValueError):
            generate_phone_numbers(-1)

    def test_invalid_number_count(self):
        with self.assertRaises(ValueError):
            generate_phone_numbers(1, 0)

    def test_invalid_phone_length(self):
        with self.assertRaises(ValueError):
            generate_phone_numbers(1, 1, -5)


if __name__ == '__main__':
    unittest.main()
