import unittest
def coin_change_max(coins, amount):
    memo = dict()
    def helper(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n < 0:
            return -1
        coin_counts = float('-INF')
        for coin in coins:
            sub = helper(n-coin)
            if sub == -1:
                continue
            coin_counts = max(coin_counts,sub+1)
        memo[n] = coin_counts if coin_counts != float('-INF') else -1
        return memo[n]
    return helper(amount)
class Test(unittest.TestCase):
    def test_coin_change_max(self):
        self.assertEqual(coin_change_max([1,2],3),3)
        self.assertEqual(coin_change_max([2,5],12),6)
        self.assertEqual(coin_change_max([2],3),-1)
        self.assertEqual(coin_change_max([2,4],7),-1)
        self.assertEqual(coin_change_max([1],0),0)
if __name__ == '__main__':
    unittest.main()