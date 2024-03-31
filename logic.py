import random
#po
class GameOfLife:
    def __init__(self, num_cells_x, num_cells_y):
        self.num_cells_x = num_cells_x
        self.num_cells_y = num_cells_y
        self.grid = [[{"organism": None, "food": 0}] * num_cells_x for _ in range(num_cells_y)]

    def place_organism(self, x, y, organism):
        if 0 <= x < self.num_cells_x and 0 <= y < self.num_cells_y:
            self.grid[y][x]["organism"] = organism

    def move_organism(self, from_x, from_y, to_x, to_y):
        if (0 <= from_x < self.num_cells_x and 0 <= from_y < self.num_cells_y) and \
           (0 <= to_x < self.num_cells_x and 0 <= to_y < self.num_cells_y):
            organism = self.grid[from_y][from_x]["organism"]
            self.grid[from_y][from_x]["organism"] = None
            self.grid[to_y][to_x]["organism"] = organism

    def update(self):
        new_grid = [[{"organism": None, "food": 0} for _ in range(self.num_cells_x)] for _ in range(self.num_cells_y)]
        for y in range(self.num_cells_y):
            for x in range(self.num_cells_x):
                cell = self.grid[y][x]
                organism = cell["organism"]

                # Count the number of neighboring organisms
                neighbors = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (dy != 0 or dx != 0) and 0 <= x + dx < self.num_cells_x and 0 <= y + dy < self.num_cells_y:
                            neighbors += bool(self.grid[y + dy][x + dx]["organism"])

                # Apply Conway's Game of Life rules
                if organism:
                    if neighbors < 2 or neighbors > 3:
                        organism = None  # Die due to underpopulation or overpopulation
                else:
                    if neighbors == 3:
                        organism = True  # Reproduction

                # Update the cell with the new organism status
                new_grid[y][x]["organism"] = organism

        # Update the grid
        self.grid = new_grid

    def get_grid(self):
        return self.grid
