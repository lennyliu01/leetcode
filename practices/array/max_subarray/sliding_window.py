#leetcode 53
import unittest
class Solution:
    def maxSubArray(self, nums):
        max_sum = sum(nums)
        curr_sum = 0
        for num in nums:
            curr_sum += num
            max_sum = max(max_sum,curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
        
class Test(unittest.TestCase):
    def test_max_sub_array(self):
        test = Solution()
        self.assertEqual(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]),6)
        self.assertEqual(test.maxSubArray([-1]),-1)
        self.assertEqual(test.maxSubArray([1]),1)
        self.assertEqual(test.maxSubArray([-1,-2]),-1)
        self.assertEqual(test.maxSubArray([5,4,-1,7,8]),23)

if __name__ == '__main__':
    unittest.main()