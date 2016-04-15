import unittest
from gpa_calc import cum_gpa

class TestGPACalculator(unittest.TestCase):

    def test_cumulative_gpa(self):
        self.assertEqual(cum_gpa(), 3.774)

if __name__ == "__main__":
    unittest.main()
