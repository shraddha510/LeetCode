class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
        
        return min_heap[0]