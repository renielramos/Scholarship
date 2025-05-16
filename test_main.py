import unittest
from main import is_eligible_for_scholarship


class TestScholarshipEligibility(unittest.TestCase):

    def test_eligible_student(self):
        self.assertTrue(is_eligible_for_scholarship(3.8, 15000))

    def test_low_gpa(self):
        self.assertFalse(is_eligible_for_scholarship(2.3, 10000))

    def test_high_income(self):
        self.assertFalse(is_eligible_for_scholarship(3.8, 50000))

    def test_high_income(self):
        self.assertTrue(is_eligible_for_scholarship(3.8, 5000))

    def test_low_gpa_high_income(self):
        self.assertFalse(is_eligible_for_scholarship(2.8, 500000))

    def test_exact_threshold(self):
        self.assertTrue(is_eligible_for_scholarship(4.0, 20000))


if __name__ == "__main__":
    unittest.main()
