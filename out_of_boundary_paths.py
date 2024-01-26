
# Leetcode : https://leetcode.com/problems/out-of-boundary-paths/

MOD_VAL = 1e9 + 7

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        total = 0
        locations = {(i, j): 1}
        for i in range(N):
            new_locations = {}
            for location, ways in locations.items():
                for delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    new_location = (location[0] + delta[0], location[1] + delta[1])
                    if self._out_of_bound(new_location, m, n):
                        total = (total + ways) % MOD_VAL
                    else:
                        if new_location not in new_locations:
                            new_locations[new_location] = 0
                        new_locations[new_location] += ways % MOD_VAL
            locations = new_locations
        return int(total)

    def _out_of_bound(self, location, m, n):
        return not(0 <= location[0] < m and 0 <= location[1] < n)
