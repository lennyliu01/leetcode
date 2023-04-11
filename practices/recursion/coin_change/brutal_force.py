import unittest
def coin_change(coins,amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    res = float('INF')
    for coin in coins:
        subproblem = coin_change(coins,amount-coin)
        if subproblem == -1: # new_amount < 0
            continue
        res = min(res,1+subproblem) #subproblem + 1 means one coin is used, coin_num += 1
    return res if res != float('INF') else -1

class Test(unittest.TestCase):
    def test_coin_change(self):
        self.assertEqual(coin_change([1,2],3),2)
        self.assertEqual(coin_change([1,2,5],11),3)
        self.assertEqual(coin_change([2],3),-1)
        self.assertEqual(coin_change([1],0),0)
        self.assertEqual(coin_change([1,2,5],32),7)
if __name__ == '__main__':
    unittest.main()
