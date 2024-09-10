class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                if nums[mid] < r:
                    r = mid - 1
                elif nums[mid] > r:
                    l = mid + 1
            elif target > nums[mid]:
                if nums[mid] < r:
                    l = mid + 1
                elif nums[mid] > r:
                    r = mid - 1
        return -1
        