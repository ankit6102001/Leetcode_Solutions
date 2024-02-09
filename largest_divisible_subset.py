
# Leetcode : https://leetcode.com/problems/largest-divisible-subset/
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n

        max_size = 1
        max_index = 0

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i

        subset = []
        while max_index != -1:
            subset.append(nums[max_index])
            max_index = prev[max_index]

        return subset[::-1]
