
# Leetcode : https://leetcode.com/problems/cherry-pickup-ii/
class Solution:
    def cherryPickup(self, grid):
        m = len(grid)
        n = len(grid[0])
        mem = [[[ -1 for _ in range(n)] for _ in range(n)] for _ in range(m)]

        # Initialize memoization array with -1
        for A in mem:
            for B in A:
                B[:] = [-1] * n

        # Start the recursion from the top-left corner of the grid
        return self.cherryPick(grid, 0, 0, n - 1, mem)

    def cherryPick(self, grid, x, y1, y2, mem):
        if x == len(grid):
            return 0

        if y1 < 0 or y1 == len(grid[0]) or y2 < 0 or y2 == len(grid[0]):
            return 0

        # Check if the result for the current state is already computed and stored in mem
        if mem[x][y1][y2] != -1:
            return mem[x][y1][y2]

        # Calculate the cherries collected in the current row for both robots
        currRow = grid[x][y1] + (0 if y1 == y2 else grid[x][y2])

        # Explore all possible moves for both robots in the next row
        for d1 in range(-1, 2):
            for d2 in range(-1, 2):
                mem[x][y1][y2] = max(mem[x][y1][y2], currRow + self.cherryPick(grid, x + 1, y1 + d1, y2 + d2, mem))

        return mem[x][y1][y2]
