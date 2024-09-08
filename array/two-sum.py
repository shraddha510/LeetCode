class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hset = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hset:
                return(hset[diff], i)
            else:
                hset[num] = i
        
        