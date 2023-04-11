import unittest
def fib(n):
    memo = [0,1]
    if not isinstance(n,int) or n < 0:
        raise ValueError(("n must be a non negative integer"))
        
    return helper(memo, n)

def helper(memo, n):
    if n == 0:
        return memo[0]
    if n == 1:
        return memo[1]
    else:
        memo.append(helper(memo,n-1) + helper(memo,n-2))
        return memo[-1]




class TestFib(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4),3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(8), 21)
        self.assertEqual(fib(9),34)
    def test_fib_negative(self):
        with self.assertRaises(ValueError): 
            fib(-1)
        with self.assertRaises(ValueError): 
            fib("")
        with self.assertRaises(ValueError):
            fib(-2)
        with self.assertRaises(ValueError):
            fib(-5)
        with self.assertRaises(ValueError):
            fib(-1.3)
        with self.assertRaises(ValueError):
            fib(0.9)

if __name__ == '__main__':
    unittest.main()