# coin change dp from bottom up
# f[0] = 0, f[1] = x, f[2] = y then f[1+2] = y +1
import unittest


def coin_change(coins, amount):
    dp = [amount + 1 ] * (amount+1)
    dp[0] = 0
    for a in range(1,amount+1):
        for coin in coins:
            if a >= coin:
                dp[a] = min(dp[a], 1 + dp[a-coin])
    print(dp)
    return dp[amount] if dp[amount] != amount + 1 else -1

print(coin_change([2,3],6))
# class Test(unittest.TestCase):
#     def test_coin_change(self):
#         self.assertEqual(coin_change([1,2],3),2)
#         self.assertEqual(coin_change([1,2,5],11),3)
#         self.assertEqual(coin_change([2],3),-1)
#         self.assertEqual(coin_change([1],0),0)
#         self.assertEqual(coin_change([1,2,5],32),7)
# if __name__ == '__main__':
#     unittest.main()
