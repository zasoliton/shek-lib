import unittest

from shek_lib import text


class TestUtils(unittest.TestCase):
    def test_hello(self):
        result = text.hello("world")
        self.assertEqual(result, "Hello world")
