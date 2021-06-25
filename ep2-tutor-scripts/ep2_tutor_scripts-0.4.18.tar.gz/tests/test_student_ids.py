import unittest
from ep2_core.common import verify_and_normalize_student_id
from result import Ok, Err


class StudentIdNormalization(unittest.TestCase):

    def test_correct_8digit_ids(self):
        self.assertEqual(Ok('11777729'), verify_and_normalize_student_id('11777729'))

    def test_correct_less_than_8digit_ids(self):
        self.assertEqual(Ok('01612345'), verify_and_normalize_student_id('1612345'))
        self.assertEqual(Ok('00612345'), verify_and_normalize_student_id('612345'))
        self.assertEqual(Ok('00612345'), verify_and_normalize_student_id('0612345'))

    def test_too_long(self):
        self.assertEqual(Err('invalid student id'), verify_and_normalize_student_id('123456789'))

    def test_invalid_characters(self):
        self.assertEqual(Err('invalid student id'), verify_and_normalize_student_id('e11777729'))


if __name__ == '__main__':
    unittest.main()
