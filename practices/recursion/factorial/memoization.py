import unittest
def factorial(n):
    product = [1]
    if not isinstance(n,int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0: #base case
        return 1
    return helper(product,n)

def helper(product,n):
    if n == 1:
        product.append(product[0]*n)
    else:
        product.append(helper(product,n-1)*n)
    return product[-1]

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4),24)
        self.assertEqual(factorial(5),120)
        self.assertEqual(factorial(6),720)
    def test_factorial_invaild_inot(self):
        with self.assertRaises(ValueError): 
            factorial(-1)
        with self.assertRaises(ValueError): 
            factorial("")
        with self.assertRaises(ValueError):
            factorial(-2)
        with self.assertRaises(ValueError):
            factorial(-5)
        with self.assertRaises(ValueError):
            factorial(-1.3)
        with self.assertRaises(ValueError):
            factorial(0.9)


if __name__ == '__main__':
    unittest.main()