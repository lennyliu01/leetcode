import unittest
# def coin_change(coins, amount):
#     memo = dict()
#     def dp(n):
#         if n in memo:
#             return memo[n]
#         if n == 0:
#             return 0
#         if n < 0: 
#             return -1
#         coin_count = float('INF')
#         for coin in coins:
#             remainder = dp(n - coin)
#             if remainder == -1:
#                 continue
#             coin_count = min(coin_count, remainder+1)
#         memo[n] = coin_count if coin_count != float('INF') else -1
#         return memo[n]
#     return dp(amount)
#print(coin_change([1,3,5],11))

def coin_change(coins, amount):
    memo = dict()  #only getting created once, the recusion happended on helper not coin_change
    return helper(memo,coins,amount)
def helper(memo,coins, amount):
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    num_of_coins = float('INF') #only execute when there is a new amount
    for coin in coins:
        sub = helper(memo,coins,amount-coin)
        if sub == -1:
            continue
        num_of_coins = min(num_of_coins, sub+1)
    memo[amount] = num_of_coins if num_of_coins != float('INF') else -1 
    return memo[amount]
# not working memo = dict() is overwritten in every recursion --no existing from the basecase
# def coin_change(coins,amount):
#     memo = dict()
#     if amount in memo:
#         return memo[amount]
#     if amount == 0:
#         return 0
#     if amount < 0:
#         return -1
#     num_of_coins = float('INF')
#     for coin in coins:
#         sub = coin_change(coins, amount - coin)
#         if sub == -1:
#             continue
#         num_of_coins = min(num_of_coins, sub+1)
#     memo[amount] = num_of_coins if num_of_coins != float('INF') else -1

class Test(unittest.TestCase):
    def test_coin_change(self):
        self.assertEqual(coin_change([1,2],3),2)
        self.assertEqual(coin_change([1,2,5],11),3)
        self.assertEqual(coin_change([2],3),-1)
        self.assertEqual(coin_change([1],0),0)
        self.assertEqual(coin_change([1,2,5],32),7)
if __name__ == '__main__':
    unittest.main()
