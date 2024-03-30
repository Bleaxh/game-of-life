import random

class GameOfLife:
    def __init__(self, num_cells_x, num_cells_y):
        self.num_cells_x = num_cells_x
        self.num_cells_y = num_cells_y
        self.grid = [[False] * num_cells_x for _ in range(num_cells_y)]

    def toggle_cell(self, x, y):
        self.grid[y][x] = not self.grid[y][x]

    def update(self):
        # Implement Game of Life rules here (e.g., Conway's rules)
        # You can evolve the grid based on the current state.

        # Placeholder: Randomly toggle cells for demonstration
        import random
        for y in range(self.num_cells_y):
            for x in range(self.num_cells_x):
                if random.random() < 0.1:
                    self.toggle_cell(x, y)

    def get_grid(self):
        return self.grid
