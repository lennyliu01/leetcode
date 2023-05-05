import unittest
#(bottom up)

class Solution:
    def wordBreak(self, s, wordDict):
        def helper(curr):
            if curr == len(s):
                return True
            if curr in memo:
                return memo[curr]
            memo[curr] = False
            for i in range(curr,len(s)+1):
                if s[curr:i] in wordDict and helper(i):
                    memo[curr] = True
                    break
            return memo[curr]
        
        memo = {}
        return helper(0)
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().wordBreak('leetcode', ["leet", "code"]), True)
        self.assertEqual(Solution().wordBreak('applepenapple', ["apple", "pen"]), True)
        self.assertEqual(Solution().wordBreak('catsandog', ["cats","dog","sand","and","cat"]), False)
        self.assertEqual(Solution().wordBreak("aaaaaaa", ["aaaa","aaa"]), True)


if __name__ == '__main__':
    unittest.main()