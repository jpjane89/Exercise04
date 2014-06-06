import unittest

from skills1 import *

class TestListOperations(unittest.TestCase):

    def setUp(self):
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                       'Sep', 'Oct', 'Nov', 'Dec']
        self.animals = ['dog', 'cat', 'pig', 'giraffe', 'elephant', 'deer']
        self.multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
        self.numbers = [-5, 1, 4, 8, -7, 11, 23, 45]
        self.positives = [1, 4, 8, 11, 23, 45]

    def test_all_odd(self):
        self.assertEqual(all_odd(self.multiples), [3, 9, 15, 21, 27])

    def test_all_even(self):
        self.assertEqual(all_even(self.multiples), [0, 6, 12, 18, 24])

    def test_long_words(self):
        self.assertEqual(long_words(self.animals), ['giraffe', 'elephant', 'deer'])

    def test_smallest(self):
        self.assertEqual(smallest(self.multiples), 0)
        self.assertEqual(smallest(self.numbers), -7)
        self.assertEqual(smallest(self.positives), 1)

    def test_largest(self):
        self.assertEqual(largest(self.multiples), 27)
        self.assertEqual(largest(self.numbers), 45)
        self.assertEqual(largest(self.positives), 45)

    def test_halvesies(self):
        self.assertEqual(halvesies(self.multiples), [0, 1.5, 3, 4.5, 6, 7.5, 9, 10.5, 12, 13.5])
        self.assertEqual(halvesies(self.numbers), [-2.5, 0.5, 2, 4, -3.5, 5.5, 11.5, 22.5])
        self.assertEqual(halvesies(self.positives), [0.5, 2, 4, 5.5, 11.5, 22.5])

    def test_word_lengths(self):
        self.assertEqual(word_lengths(self.months), [3] * 12)
        self.assertEqual(word_lengths(self.animals), [3, 3, 3, 7, 8, 4])

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(self.multiples), 135)
        self.assertEqual(sum_numbers(self.numbers), 80)

    def test_mult_numbers(self):
        self.assertEqual(mult_numbers(self.multiples), 0)
        self.assertEqual(mult_numbers(self.numbers), 12751200)

    def test_join_strings(self):
        self.assertEqual(join_strings(self.months), "JanFebMarAprMayJunJulAugSepOctNovDec")
        self.assertEqual(join_strings(self.animals), "dogcatpiggiraffeelephantdeer")

    def test_average(self):
        self.assertEqual(average(self.multiples), 13.5)
        self.assertEqual(average(self.numbers), 10)

if __name__ == '__main__':
    unittest.main()
