import unittest
from  GCD import get_gcd

class TestGCDMethod(unittest.TestCase):
    # Test cases
    def test_gcd(self):
        test_cases = [
            (36, 60, 12),
            (48, 180, 12),
            (120, 45, 15),
            (81, 153, 9),
            (250, 625, 125),
            (1024, 2048, 1024),
            (144, 233, 1),
            (315, 945, 315)
        ]

        # Loop through each test case and assert if the output is correct
        for num1, num2, expected_gcd in test_cases:
            with self.subTest(f"GCD of {num1} and {num2}"):
                self.assertEqual(get_gcd(num1, num2), expected_gcd)


# To run the tests
if __name__ == '__main__':
    unittest.main()
