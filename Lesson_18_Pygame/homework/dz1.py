import pygame


class Dz1:
    def __init__(self, n: int, screen_width: int = 300, screen_height: int = 300) -> None:
        pygame.init()
        self.width: int = screen_width
        self.height: int = screen_height
        self.n = n
        self.screen: pygame.Surface = pygame.display.set_mode((self.width, self.height))
        self.game_end = False
        self.line_color = (255, 255, 255)
        self.radius = min(self.width, self.height) // 2 - 20
        self.center_x, self.center_y = self.width // 2, self.height // 2

    def run(self) -> None:
        while not self.game_end:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_end = True
        pygame.quit()
        exit()

    def draw(self) -> None:
        width1 = 40
        height1 = 300
        x = 136.5
        y = 0

        pygame.draw.ellipse(self.screen, (255, 255, 255), (0, 0, 300, 300), 1)
        pygame.display.flip()
        for i in range(1, self.n):
            pygame.draw.ellipse(self.screen, (255, 255, 255), (x, y, width1, height1), 1)
            pygame.draw.ellipse(self.screen, (255, 255, 255), (y, x, height1, width1), 1)
            pygame.display.flip()
            width1 += 28
            x -= 15
        pygame.display.flip()


def main():
    try:
        n = int(input())
        dz1 = Dz1(n)
        dz1.run()
    except ValueError:
        print("Неправильный формат ввода")
        exit()


if __name__ == "__main__":
    main()