import pygame


class cl1:
    def __init__(self, screen_width: int, screen_height: int) -> None:
        pygame.init()
        self.width: int = screen_width
        self.height: int = screen_height
        self.screen: pygame.Surface = pygame.display.set_mode((self.width, self.height))
        self.background = (0, 0, 255)
        self.game_end = False

        self.circles = []

    def run(self) -> None:
        while not self.game_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_end = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.circles.clear()
                    self.circles.append([event.pos, 0])
            self.screen.fill((0, 0, 255))
            new_circles = []

            for pos, radius in self.circles:
                pygame.draw.circle(self.screen, (255, 255, 0), pos, int(radius))
                radius += 0.02
                new_circles.append([pos, radius])
            self.circles = new_circles
            pygame.display.flip()

        pygame.quit()
        exit()


def main():
    size = 800
    dz1 = cl1(size, size)
    dz1.run()


if __name__ == "__main__":
    main()