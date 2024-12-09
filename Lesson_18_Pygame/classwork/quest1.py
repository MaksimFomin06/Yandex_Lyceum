import pygame


class Quest1:
    def __init__(self, screen_width: int, screen_height: int) -> None:
        pygame.init()
        self.width: int = screen_width
        self.height: int = screen_height
        self.screen: int = pygame.display.set_mode((self.width, self.height))
        self.game_end: bool = False
        self.draw_color: tuple = (255, 255, 255)

    def run(self) -> None:
        while not self.game_end:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_end = True

    def draw(self) -> None:
        pygame.draw.line(self.screen, self.draw_color, (0, 0), (self.width, self.height), 5)
        pygame.draw.line(self.screen, self.draw_color, (0, self.height), (self.width, 0), 5)
        pygame.display.flip()


def main():
    try:
        num1 = int(input("Введите ширину окна: "))
        num2 = int(input("Введите высоту окна: "))
        quest1 = Quest1(num1, num2)
        quest1.run()
    except ValueError:
        print("Неправильный формат ввода")
        exit()


if __name__ == "__main__":
    main()
