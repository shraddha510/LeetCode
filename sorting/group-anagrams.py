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
        anagrams = defaultdict(list)
        
        # Iterate through each string in the list
        for word in strs:
            # Sort the word to form the key
            sorted_word = ''.join(sorted(word))
            # Add the original word to the list of its sorted version
            anagrams[sorted_word].append(word)
        
        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())

            
                

