""" Comment """
import unittest
import transform


""" Comment """
class TestStringMethods(unittest.TestCase):

""" Comment """
    def test_is_upper(self):
        sting = transform.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")

""" Comment """
    def test_is_lower(self):
        sting = transform.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")

""" Comment """
    def test_is_capitalize(self):
        sting = transform.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")


if __name__ == '__main__':
    unittest.main()
