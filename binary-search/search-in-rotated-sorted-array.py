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

            # If we found the target
            if nums[mid] == target:
                return mid

            # Check if the left half is sorted
            if nums[l] <= nums[mid]:
                # Target is in the left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Otherwise, the right half must be sorted
            else:
                # Target is in the right half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1  # Target not found
