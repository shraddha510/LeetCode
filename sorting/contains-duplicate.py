class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        hashset 
        iterate through the array 
        as soon as we hit an elem already in the hashset, return true
        '''

        hset = set()

        for num in nums:
            if num in hset:
                return True
            else:
                hset.add(num)
        return False