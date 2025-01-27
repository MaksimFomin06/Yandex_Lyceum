import pygame


class Rhombuses:
    def __init__(self, rhomb_size):
        self.__width = 300
        self.__height = 300
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.game_end = False

        self.__bg_color = (255, 255, 0)

        self.rhomb_size = (rhomb_size, rhomb_size)
        self.rhomb_color = (255, 128, 0)
        self.rhomb_quantity = 0

    def run(self):
        while not self.game_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_end = True
            self.draw()
    
    def draw(self):
        self.__screen.fill(self.__bg_color)
        pygame.draw.rect(self.__screen, self.rhomb_color, (0, 0, 30, 30))
        pygame.display.flip()


def main():
    try:
        rhomb_size = int(input())
        app = Rhombuses(rhomb_size)
        app.run()

    except ValueError:
        print("Неправильный формат ввода")


if __name__ == "__main__":
    main()