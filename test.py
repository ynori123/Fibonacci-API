from app import fibonacci
import unittest

class Test(unittest.TestCase):
    def test_first_fib(self):
        result = fibonacci(1)
        self.assertEqual(result, 1)
    def test_second_fib(self):
        result = fibonacci(2)
        self.assertEqual(result, 1)
    def test_third_fib(self):
        result = fibonacci(3)
        self.assertEqual(result, 2)
    def test_fourth_fib(self):
        result = fibonacci(4)
        self.assertEqual(result, 3)
    def test_fifth_fib(self):
        result = fibonacci(5)
        self.assertEqual(result, 5)
    def test_large_fib(self):
        result = fibonacci(100)
        self.assertEqual(result, 354224848179261915075)
    def test_largelarge_fib(self):
        result = fibonacci(200)
        self.assertEqual(result, 280571172992510140037611932413038677189525)
    
if __name__=='__main__':
    unittest.main()