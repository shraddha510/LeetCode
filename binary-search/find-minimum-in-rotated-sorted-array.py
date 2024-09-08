class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        curr_min = float("inf")

        while l < r:
            mid = l + (r - l) // 2
            curr_min = min(curr_min, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid - 1
        
        return min(curr_min, nums[l])