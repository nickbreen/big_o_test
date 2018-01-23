import unittest
import big_o
from solution import solution

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(solution(9), 2)
        self.assertEqual(solution(529), 4)
        self.assertEqual(solution(20), 1)
        self.assertEqual(solution(15), 0)
        self.assertEqual(solution(1041), 5)

    def testPerf(self):
        gen = lambda n: big_o.datagen.large_integers(n)
        best, others = big_o.big_o(solution, gen, n_repeats=100)
        self.assertEqual(big_o.complexities.Linear, best)

if __name__ == '__main__':
    unittest.main()
