import logging
import unittest

from fill_params import fill_randomly
from src.utils.ip_generator import Ip
from src.utils.url_generate import Url

logging.basicConfig(level=logging.DEBUG)


class TestDecorators(unittest.TestCase):
    def test_decorator_with_int(self):
        @fill_randomly
        def my_func(number: int):
            return number

        result = my_func()
        logging.debug(f"Number: {result}")
        self.assertIsNotNone(result)

    def test_decorator_with_str(self):
        @fill_randomly
        def my_func(text: str):
            return text

        result = my_func()
        logging.debug(f"Text: {result}")
        self.assertIsNotNone(result)

    def test_decorator_with_url(self):
        @fill_randomly
        def my_func(url: Url):
            return url

        result = my_func()
        logging.debug(f"Url: {result}")
        self.assertIsNotNone(result)

    def test_decorator_with_json(self):
        @fill_randomly
        def my_func(json: dict):
            return json

        result = my_func()
        logging.debug(f"Json: {result}")
        self.assertIsNotNone(result)

    def test_decorator_with_ip(self):
        @fill_randomly
        def my_func(ip: Ip):
            return ip

        result = my_func()
        logging.debug(f"Ip: {result}")
        self.assertIsNotNone(result)

    def test_decorator_with_multiple_params(self):
        @fill_randomly
        def my_func(number: int, text: str, url: Url):
            return number, text, url

        result = my_func()
        logging.debug(f"Result: {result}")
        self.assertIsNotNone(result)
