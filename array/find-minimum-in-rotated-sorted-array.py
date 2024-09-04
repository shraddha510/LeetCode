class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) -1
        curr_min = float("inf")

        while start < end:
            mid = start + (end - start) // 2
            curr_min = min(curr_min, nums[mid])

            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid - 1
        
        return min(curr_min, nums[start])

            