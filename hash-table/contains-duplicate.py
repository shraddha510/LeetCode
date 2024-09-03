class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hset = set()

        for num in nums:
            if num in hset:
                return True
            else:
                hset.add(num)
        return False