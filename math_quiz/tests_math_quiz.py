import unittest
from math_quiz import generate_random_integer, get_random_operator, create_problem_and_answer


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        # Test if the operator is one of the expected symbols
        valid_operators = ['+', '-', '*']
        for _ in range(100):  # Check multiple random selections
            operator = get_random_operator()
            self.assertIn(operator, valid_operators)

    def test_create_problem_and_answer(self):
        # Test cases for different operators
        test_cases = [
            (5, 2, '+', "5 + 2", 7),     # Addition
            (5, 2, '-', "5 - 2", 3),     # Subtraction
            (5, 2, '*', "5 * 2", 10)     # Multiplication
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_problem_and_answer(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
