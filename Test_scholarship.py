import unittest
from Scholarship import is_eligible_for_scholarship


class TestScholarshipEligibility(unittest.TestCase):

    def test_eligible_student(self):
        self.assertTrue(is_eligible_for_scholarship(3.8, 15000))

    def test_low_gpa(self):
        self.assertFalse(is_eligible_for_scholarship(2.3, 10000))

    def test_low_gpa(self):
        self.assertTrue(is_eligible_for_scholarship(5.0, 100000))

    def test_high_income(self):
        self.assertFalse(is_eligible_for_scholarship(3.8, 50000))
