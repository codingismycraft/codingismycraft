"""Solves the Max Area of Island problem.

https://leetcode.com/problems/max-area-of-island/
"""


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dsf():
            queue.clear()
            queue.append((row, col))
            area = 0
            while queue:
                item = queue.pop(0)
                if item in visited:
                    continue
                area += 1
                visited.add(item)
                for dx, dy in _NEIGHBORS:
                    neighbour = item[0] + dx, item[1] + dy
                    if neighbour not in visited:
                        if 0 <= neighbour[0] < num_rows and 0 <= neighbour[
                            1] < num_cols:
                            if grid[neighbour[0]][neighbour[1]] == 1:
                                queue.append(neighbour)
            return area

        max_area = 0
        _NEIGHBORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        num_rows = len(grid)
        num_cols = len(grid[0])
        counter = 0
        visited = set()
        queue = []
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] != 1 or (row, col) in visited:
                    continue
                r = dsf()
                counter += 1
                max_area = max(max_area, r)
        return max_area
