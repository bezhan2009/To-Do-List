import logging
import unittest

from datagen.src.generators.random_data.random_data import random_data

logging.basicConfig(level=logging.DEBUG)


class TestRandomData(unittest.TestCase):
    def test_random_data_int(self):
        generated_int = random_data(int)
        logging.debug(f"Generated int: {generated_int}")
        self.assertIsInstance(generated_int, int)

    def test_random_data_float(self):
        generated_float = random_data(float)
        logging.debug(f"Generated float: {generated_float}")
        self.assertIsInstance(generated_float, float)

    def test_random_data_str(self):
        generated_str = random_data(str, 10)
        logging.debug(f"Generated str: {generated_str}")
        self.assertIsInstance(generated_str, str)
        self.assertEqual(len(generated_str), 10)

    def test_data_type_error(self):
        with self.assertRaises(ValueError):
            random_data("")
