"""Solves the number of islands.

See also https://leetcode.com/problems/number-of-islands/
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dsf():
            queue.clear()
            queue.append((row, col))
            while queue:
                item = queue.pop(0)
                if item in visited:
                    continue
                visited.add(item)
                for dx, dy in _NEIGHBORS:
                    neighbour = item[0] + dx, item[1] + dy
                    if neighbour not in visited:
                        if 0 <= neighbour[0] < num_rows and 0 <= neighbour[1] < num_cols:
                            if grid[neighbour[0]][neighbour[1]] == "1":
                                queue.append(neighbour)

        _NEIGHBORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        num_rows = len(grid)
        num_cols = len(grid[0])
        counter = 0
        visited = set()
        queue = []
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] != "1" or (row, col) in visited:
                    continue
                dsf()
                counter += 1
        return counter

