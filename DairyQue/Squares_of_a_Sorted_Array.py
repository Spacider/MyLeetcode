# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
#
#
# Example 1:
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for index in range(len(nums)):
            nums[index] = (nums[index] * nums[index])

        return sorted(nums)




if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    nums = Solution.sortedSquares(nums, nums)
    print(nums)