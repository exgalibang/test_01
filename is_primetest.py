from count import is_prime
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        number = input('Enter a number: ')
        self.number = int (number)

    def test_case(self):
        self.assertTrue(is_prime(self.number),msg = 'Is not prime')

    def tearDown(self):
        print('test end')

if __name__ == '__main__':
    unittest.main()
