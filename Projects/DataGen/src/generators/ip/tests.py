import logging
import unittest

from datagen.src.generators.ip.dataclass import Ip
from datagen.src.generators.ip.generator import ipv4_generate, ipv6_generate

logging.basicConfig(level=logging.DEBUG)


class TestIpGenerator(unittest.TestCase):
    def test_ipv4_generate(self):
        generated_ipv4: Ip = ipv4_generate()
        logging.debug(f"Generated ipv4: {generated_ipv4}")
        self.assertEqual(generated_ipv4.type, "ipv4")
        self.assertTrue(generated_ipv4.valid())

    def test_ipv4_generate_invalid(self):
        generated_ipv4: Ip = ipv4_generate(False)
        logging.debug(f"Generated ipv4: {generated_ipv4}")
        self.assertEqual(generated_ipv4.type, "ipv4")
        self.assertFalse(generated_ipv4.valid())

    def test_ipv6_generate(self):
        generated_ipv6: Ip = ipv6_generate()
        logging.debug(f"Generated ipv6: {generated_ipv6}")
        self.assertEqual(generated_ipv6.type, "ipv6")
        self.assertTrue(generated_ipv6.valid())

    def test_ipv6_generate_invalid(self):
        generated_ipv6: Ip = ipv6_generate(False)
        logging.debug(f"Generated ipv6: {generated_ipv6}")
        self.assertEqual(generated_ipv6.type, "ipv6")
        self.assertFalse(generated_ipv6.valid())
