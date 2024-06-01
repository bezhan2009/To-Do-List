import logging
import unittest

from datagen.src.generators.json.generator import generate_json

logging.basicConfig(level=logging.DEBUG)


class TestJsonGenerator(unittest.TestCase):
    def test_json_generate(self):
        generated_json = generate_json()
        logging.debug(f"Generated json: {generated_json}")
        self.assertIsInstance(generated_json, dict)
        self.assertEqual(len(generated_json), 10)

    def test_json_generate_error(self):
        with self.assertRaises(ValueError):
            generate_json(-1)

    def test_json_generate_error_type(self):
        with self.assertRaises(ValueError):
            generate_json("10")
