class GameOfLife:
    def __init__(self, num_cells_x, num_cells_y):
        self.num_cells_x = num_cells_x
        self.num_cells_y = num_cells_y
        self.grid = [[None] * num_cells_x for _ in range(num_cells_y)]

    def add_organism(self, organism):
        if 0 <= organism.x < self.num_cells_x and 0 <= organism.y < self.num_cells_y:
            self.grid[organism.y][organism.x] = organism

    def update(self):
        # Implement game logic (e.g., move organisms, interactions, evolution)
        pass

    def get_grid(self):
        return self.grid
