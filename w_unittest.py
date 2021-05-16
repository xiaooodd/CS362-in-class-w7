import unittest
import wordcount

class TestName(unittest.TestCase):
    def test1(self):
        self.assertEqual(wordcount.w_count("Hello world!"), 2)

    def test2(self):
        self.assertEqual(wordcount.w_count(" Hello, my name is Tom! "), 5)

    def test3(self):
        self.assertEqual(wordcount.w_count("!Hello,4564 Tom! "), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)