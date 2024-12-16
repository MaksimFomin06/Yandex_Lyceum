import pygame

class BrickWall:
    def __init__(self, screen_width: int, screen_height: int, brick_size: tuple, gap_size: int):
        pygame.init()
        self.width = screen_width
        self.height = screen_height
        self.brick_size = brick_size
        self.gap_size = gap_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.game_end = False

    def run(self):
        while not self.game_end:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_end = True
        pygame.quit()
        exit()

    def draw(self):
        bricks_per_row = (self.width - self.gap_size) // (self.brick_size[0] + self.gap_size)
        rows_per_wall = (self.height - self.gap_size) // (self.brick_size[1] + self.gap_size)
        wall_count = 0
        while wall_count < rows_per_wall:
            row_offset = wall_count % 2 * (self.brick_size[0] + self.gap_size)
            for col in range(bricks_per_row):
                x = row_offset + col * (self.brick_size[0] + self.gap_size)
                y = wall_count * (self.brick_size[1] + self.gap_size)
                rect = pygame.Rect(x, y, self.brick_size[0], self.brick_size[1])
                pygame.draw.rect(self.screen, (255, 0, 0), rect)
            wall_count += 1
        pygame.display.flip()

def main():
    try:
        screen_width = 300
        screen_height = 200
        brick_size = (30, 15)
        gap_size = 2
        brick_wall = BrickWall(screen_width, screen_height, brick_size, gap_size)
        brick_wall.run()
    except ValueError:
        print("Неправильный формат ввода")
        exit()

if __name__ == "__main__":
    main()