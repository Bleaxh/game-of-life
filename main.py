import sys
import sdl2
import sdl2.ext
from logic import GameOfLife

def main():
    try:
        sdl2.ext.init()

        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        CELL_SIZE = 10

        window = sdl2.ext.Window("Game of Life", size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        window.show()

        renderer = sdl2.ext.Renderer(window)

        WHITE = sdl2.ext.Color(255, 255, 255)
        BLACK = sdl2.ext.Color(0, 0, 0)

        game_of_life = GameOfLife(SCREEN_WIDTH // CELL_SIZE, SCREEN_HEIGHT // CELL_SIZE)

        # Game loop
        running = True
        while running:
            for event in sdl2.ext.get_events():
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break

            # Update the game logic (e.g., evolve the grid)
            game_of_life.update()

            # Clear the screen
            renderer.clear(BLACK)

            # Draw the grid
            for y in range(game_of_life.num_cells_y):
                for x in range(game_of_life.num_cells_x):
                    if game_of_life.get_grid()[y][x]:
                        # Draw a live cell
                        renderer.fill((x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), WHITE)
                    else:
                        # Draw a dead cell
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
