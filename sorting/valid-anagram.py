class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hset1 = {}
        hset2 = {}

        for char in s:
            if char in hset1:
                hset1[char] += 1
            else:
                hset1[char] = 1
        for char in t:
            if char in hset2:
                hset2[char] += 1
            else:
                hset2[char] = 1
        
        if hset1 == hset2:
            return True
        else:
            return False