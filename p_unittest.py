import unittest
import palindrome

class TestName(unittest.TestCase):
    def test1(self):
        self.assertEqual(palindrome.is_p(""), "Empty string")

    def test2(self):
        self.assertEqual(palindrome.is_p("mam+mam"), True)

    def test3(self):
        self.assertEqual(palindrome.is_p("masssskd"), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)