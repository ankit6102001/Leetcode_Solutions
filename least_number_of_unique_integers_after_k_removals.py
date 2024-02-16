
# Leetcode :https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        minHeap = list(collections.Counter(arr).values())
        heapq.heapify(minHeap)

        while k > 0:
          k -= heapq.heappop(minHeap)

        return len(minHeap) + (1 if k < 0 else 0)
