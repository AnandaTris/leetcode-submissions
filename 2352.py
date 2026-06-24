class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_freq = {}
        for i in range(n):
            key = tuple(grid[i])
            row_freq[key] = row_freq.get(key, 0) + 1
        count = 0
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            count += row_freq.get(col, 0)
        return count
