import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_calculator_memory_can_store(self):
        self.calculator.store_in_memory(5)
        self.assertEqual(self.calculator.peek_at_memory(), 5)

    def test_calculator_memory_peek_doesnt_remove_from_memory(self):
        self.calculator.store_in_memory(5)
        self.calculator.store_in_memory(12)
        self.assertEqual(self.calculator.peek_at_memory(), 12)
        self.assertEqual(self.calculator.peek_at_memory(), 12)

    def test_calculator_memory_can_remove(self):
        self.calculator.store_in_memory(5)
        self.calculator.store_in_memory(12)
        self.assertEqual(self.calculator.read_from_memory(), 12)
        self.assertEqual(self.calculator.read_from_memory(), 5)

    def test_calculator_can_add_two_numbers(self):
        self.fail("Not Tested yet")

    def test_calculator_can_add_two_strings(self):
        self.fail("Not Tested yet")

    def test_calculator_can_add_string_to_numbers(self):
        self.fail("Not Tested yet")

    def test_calculator_can_add_two_integers(self):
        self.fail("Not Tested yet")


if __name__ == "__main__":
    unittest.main()

