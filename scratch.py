def fizz_buzz(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

    result = ""

    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"

    return result or str(number)


# Unit Tests
import unittest


class TestFizzBuzz(unittest.TestCase):

    def test_single_number(self):
        self.assertEqual(fizz_buzz(1), '1')
        self.assertEqual(fizz_buzz(2), '2')

    def test_multiple_of_three(self):
        self.assertEqual(fizz_buzz(3), 'Fizz')
        self.assertEqual(fizz_buzz(6), 'Fizz')

    def test_multiple_of_five(self):
        self.assertEqual(fizz_buzz(5), 'Buzz')
        self.assertEqual(fizz_buzz(10), 'Buzz')

    def test_multiple_of_three_and_five(self):
        self.assertEqual(fizz_buzz(15), 'FizzBuzz')

    def test_negative_number(self):
        self.assertEqual(fizz_buzz(-3), 'Fizz')
        self.assertEqual(fizz_buzz(-5), 'Buzz')
        self.assertEqual(fizz_buzz(-15), 'FizzBuzz')

    def test_zero(self):
        self.assertEqual(fizz_buzz(0), 'FizzBuzz')  # Zero is a multiple of both 3 and 5

    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            fizz_buzz(2.5)
        with self.assertRaises(ValueError):
            fizz_buzz("three")


if __name__ == '__main__':
    unittest.main()