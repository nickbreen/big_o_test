import unittest
import big_o
import solution

class Test(unittest.TestCase):

    def testPerfLinear(self):
        gen = lambda n: big_o.datagen.integers(n, 1, 100)
        best, others = big_o.big_o(solution.linear, gen, n_repeats=100)
        self.assertIsInstance(best, big_o.complexities.Linear)

    def testPerfQuad(self):
        gen = lambda n: big_o.datagen.integers(n, 1, 100)
        best, others = big_o.big_o(solution.quad, gen, n_repeats=10, min_n=100, max_n=1000)
        self.assertIsInstance(best, big_o.complexities.Quadratic)

if __name__ == '__main__':
    unittest.main()
