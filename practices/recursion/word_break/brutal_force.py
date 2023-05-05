import unittest
#### greedy solution does not work
# class Solution:
#     def wordBreak(self, s, wordDict):
#         res = []
#         i, j = 1,0
#         for i in range(0,len(s)+1):
#             if s[j:i] in wordDict:
#                 res.append(s[j:i])
#                 j = i
#         #return s 
#         return True if ''.join(res) == s else False
# test = Solution()
# print(test.wordBreak("leetcode", ["leet", "code"]))
# print(test.wordBreak("applepenapple", ["apple", "pen"]))
# print(test.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
# print(test.wordBreak("aaaaaaa", ["aaaa","aaa"]))


# class Solution:
#     def wordBreak(self, s, wordDict):
#         # recurrsion 解法,TLE
#         def dfs(start):
#             if start == len(s):
#                 return True
            
#             for i in range(start+1,len(s)+1):
#                 if s[start:i] in wordDict and dfs(i):
#                     return True
#             return False
    
#         return dfs(0)


class Solution:
    def wordBreak(self, s, wordDict):
        def helper(start):
            if start == len(s):
                return True
            for i in range(start+1, len(s)+1):
                if s[start:i] in wordDict and helper(i):
                    return True
            return False
        return helper(0)

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().wordBreak('leetcode', ["leet", "code"]), True)
        self.assertEqual(Solution().wordBreak('applepenapple', ["apple", "pen"]), True)
        self.assertEqual(Solution().wordBreak('catsandog', ["cats","dog","sand","and","cat"]), False)
        self.assertEqual(Solution().wordBreak("aaaaaaa", ["aaaa","aaa"]), True)


if __name__ == '__main__':
    unittest.main()