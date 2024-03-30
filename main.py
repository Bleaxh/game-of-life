import sys
import sdl2
import sdl2.ext
import random
from logic import GameOfLife

def main():
    try:
        sdl2.ext.init()

        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        CELL_SIZE = 10

        window = sdl2.ext.Window("Evolutionary Simulation", size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        window.show()

        renderer = sdl2.ext.Renderer(window)

        WHITE = sdl2.ext.Color(255, 255, 255)
        BLACK = sdl2.ext.Color(0, 0, 0)

        evolutionary_simulation = GameOfLife(SCREEN_WIDTH // CELL_SIZE, SCREEN_HEIGHT // CELL_SIZE)

        # Place initial organisms
        for _ in range(50):
            x = random.randint(0, evolutionary_simulation.num_cells_x - 1)
            y = random.randint(0, evolutionary_simulation.num_cells_y - 1)
            evolutionary_simulation.place_organism(x, y, True)

        # Game loop
        running = True
        while running:
            for event in sdl2.ext.get_events():
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break

            # Update the game logic (e.g., evolve the grid)
            evolutionary_simulation.update()

            # Clear the screen
            renderer.clear(BLACK)

            # Draw the grid
            for y in range(evolutionary_simulation.num_cells_y):
                for x in range(evolutionary_simulation.num_cells_x):
                    cell = evolutionary_simulation.grid[y][x]
                    if cell["organism"]:
                        renderer.fill((x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), WHITE)
                    elif cell["food"] > 0:
                        renderer.fill((x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), (0, 255, 0))
                    else:
                        renderer.draw_rect((x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), WHITE)

            # Update the display
            renderer.present()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sdl2.ext.quit()
        sys.exit()

if __name__ == "__main__":
    main()
