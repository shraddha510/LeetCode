class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hmap1 = {}
        hmap2 = {}

        for char in s:
            if char in hmap1:
                hmap1[char] += 1
            hmap1[char] = 1
        for char in t:
            if char in hmap2:
                hmap2[char] += 1
            hmap2[char] = 1
        if hmap1 == hmap2:
            return True
        return False
        