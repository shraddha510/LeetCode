class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hmap:
                return i, hmap[diff]
            else:
                hmap[num] = i