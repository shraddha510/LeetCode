class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        create hmap
        create count array and increment the count for each letter
        store count as a tuple "key"

        """
        hmap = {}

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
            key = tuple(count)
            if key in hmap:
                hmap[key].append(s)
            else:
                hmap[key] = [s]
        return list(hmap.values())
        
            

