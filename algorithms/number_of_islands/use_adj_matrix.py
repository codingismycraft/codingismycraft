_NEIGHBORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_rows = len(grid)
        num_cols = len(grid[0])
        counter = 0
        visited = set()
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dsf(grid, row, col, num_rows, num_cols, visited)
                    counter += 1
        return counter


def dsf(grid, row, col, num_rows, num_cols, visited):
    queue = [(row, col)]
    while queue:
        item = queue.pop(0)
        if item not in visited:
            visited.add(item)
            for dx, dy in _NEIGHBORS:
                row, col = item[0] + dx, item[1] + dy
                if 0 <= row < num_rows and 0 <= col < num_cols:
                    if grid[row][col] == "1" and (row, col) not in visited:
                        queue.append((row, col))
