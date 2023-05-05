#300. Longest Increasing Subsequence
# class Solution:
#     def lengthOfLIS(self, nums):
#         if not all(isinstance(num, int) for num in nums):
#             return ValueError('Numbers have to be integers.')
#         if len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return 1
#         for i in range(len(nums)-1):
#             self.count = 0
#             for num in nums[:i+1]:
#                 print(num, nums[i+1])
#                 if num < nums[i+1]:
#                     self.count += 1
#         return self.count

# test = Solution()
# print(test.lengthOfLIS([10,9,2,5,3,7,101,18]))

    # def helper(self,nums):
    #     if len(nums) == 1:
    #         return 1
    #     for i in range(len(nums)-1):
    #         print(f"loop {i}")
    #         for num in nums[:i+1]:
    #             print(num, nums[i])
    #             if num < nums[i]:
    #                 res = self.helper(nums[:i+1]) +1
    #     return res
    # def helper(self,nums):
    #     if len(nums) == 1:
    #         return 1
    #     for i in range(0,len(nums)-1):
    #         res = self.helper(nums[i+1:])
    #         for num in nums[i+1:]:
    #             print(nums[i],num)
    #             if nums[i] < num:
    #                 self.count = max(res, res+1)
    #     return self.count
    # def helper(self,nums):
    #     if len(nums) == 1:
    #         return 1
    #     for i in range(len(nums)-1):
    #         sub = self.helper(nums[i+1:])
    #         for num in nums[i+1:]:
    #             print(num, nums[i+1])
    #             if num < nums[i]:
    #                 sub += 1
    #     return sub


# class Solution():
#     def lengthOfLIS(self,seq):
#             return self.find_longest_incresing_subsequence_recursion_util(seq, 0, -1)


#     def find_longest_incresing_subsequence_recursion_util(self,seq, current, prev):
#         if (current == len(seq)):
#             return 0

#         current_included_count = 0
#         if (prev == -1 or seq[current] >= seq[prev]):
#             current_included_count = 1 + self.find_longest_incresing_subsequence_recursion_util(seq, current + 1, current)

#         current_excluded_count = self.find_longest_incresing_subsequence_recursion_util(seq, current + 1, prev)

#         return max(current_included_count, current_excluded_count)
# test = Solution()
# print(test.lengthOfLIS([10,9,2,5,3,7,101,18]))




class Solution():
    def lengthOfLIS(self,nums):
            return self.helper(nums, 0, -1)


    def helper(self,nums, current, prev):
        if current == len(nums):
            return 0
        curr_count = 0
        if prev == -1 or nums[current] > nums[prev]:
            curr_count = 1 + self.helper(nums, current + 1, current)
        curr_excluded_count = self.helper(nums, current + 1, prev)

        return max(curr_count, curr_excluded_count)
test = Solution()
print(test.lengthOfLIS([10,9,2,5,3,7,101,18]))