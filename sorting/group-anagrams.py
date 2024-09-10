class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hmap = defaultdict(list)

        for word in strs:
            sort = ''.join(sorted(word))
            hmap[sort].append(word)

        return list(hmap.values())