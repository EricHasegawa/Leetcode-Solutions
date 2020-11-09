class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    numIslands += Solution.dfs(self, grid, i, j)
        return numIslands
    
    def dfs(self, grid: List[List[str]], i: int, j: int) -> int:
        # if we are out of bounds, or in water, return 0
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
            return 0
        # "sink" the islands so they are not revisited
        grid[i][j] = "0"
        Solution.dfs(self, grid, i + 1, j)
        Solution.dfs(self, grid, i - 1, j)
        Solution.dfs(self, grid, i, j + 1)
        Solution.dfs(self, grid, i, j - 1)
        return 1
