import pygame


class Quest2:
    def __init__(self, screen_width: int, screen_height: int) -> None:
        self.width: int = screen_width
        self.height: int = screen_height
        self.screen: pygame.display = pygame.display.set_mode((self.width, self.height))
        self.game_end: bool = False
        self.draw_color: tuple = (255, 0, 0)
    
    def run(self) -> None:
        while not self.game_end:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_end = True
    
    def draw(self) -> None:
        pygame.draw.rect(self.screen, self.draw_color, (1, 1 , self.width -1, self.height -1))
        pygame.display.flip()


def main():
    try:
        num1 = int(input("Введите ширину окна: "))
        num2 = int(input("Введите высоту окна: "))
        quest2 = Quest2(num1, num2)
        quest2.run()
    except ValueError:
        print("Неправильный формат ввода")
        exit()


if __name__ == "__main__":
    main()
