import logging
import unittest

from src.generators.url.dataclass import Url
from src.generators.url.generator import generate_url

logging.basicConfig(level=logging.DEBUG)


class TestUrlGenerator(unittest.TestCase):
    def test_generate_url(self):
        generated_url = generate_url(15)
        logging.debug(f"Generated url: {generated_url}")
        self.assertIsInstance(generated_url, Url)
        self.assertEqual(len(generated_url.full_address), 15)

    def test_generate_url_error(self):
        with self.assertRaises(ValueError):
            generate_url(-1)

    def test_generate_url_error_type(self):
        with self.assertRaises(ValueError):
            generate_url("10")

    def test_generate_url_error_too_short(self):
        with self.assertRaises(ValueError):
            generate_url(5)
