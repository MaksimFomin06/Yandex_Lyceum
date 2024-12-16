import pygame


class Quest3:
    def __init__(self, screen_width: int, screen_height: int, cells: int) -> None:
        pygame.init()
        self.width: int = screen_width
        self.height: int = screen_height
        self.cells: int = cells
        self.cell_size: int = screen_width // cells
        self.screen: pygame.Surface = pygame.display.set_mode((self.width, self.height))
        self.game_end: bool = False
        self.black: tuple = (0, 0, 0)
        self.white: tuple = (255, 255, 255)

    def run(self) -> None:
        while not self.game_end:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_end = True
        pygame.quit()
        exit()

    def draw(self) -> None:
        for row in range(self.cells):
            for col in range(self.cells):
                color = self.black if (row + col) % 2 == 0 else self.white
                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        col * self.cell_size,
                        row * self.cell_size,
                        self.cell_size,
                        self.cell_size
                    )
                )
        pygame.display.flip()


def main():
    try:
        input_data = input().strip()
        size, cells = map(int, input_data.split())

        quest3 = Quest3(size, size, cells)
        quest3.run()
    except ValueError:
        print("Неправильный формат ввода")
        exit()


if __name__ == "__main__":
    main()