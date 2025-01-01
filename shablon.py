import pygame


class Shablon:
    def __init__(self, screen_width: int, screen_height: int) -> None:
        pygame.init()
        self.width: int = screen_width
        self.height: int = screen_height
        self.screen: pygame.Surface = pygame.display.set_mode((self.width, self.height))
        self.game_end = False

    def run(self) -> None:
        while not self.game_end:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_end = True
        pygame.quit()
        exit()

    def draw(self) -> None:
        
        pygame.display.flip()


def main():
    size = 600
    dz1 = Shablon(size, size)
    dz1.run()


if __name__ == "__main__":
    main()