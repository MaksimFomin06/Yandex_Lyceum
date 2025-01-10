import pygame


class Bricks:
    def __init__(self):
        self.width = 300
        self.height = 200
        self.__screen = pygame.display.set_mode((self.width, self.height))
        self.game_end = False

        self.brick_size_pos = (100, 100, 30, 15)
        self.layer_size = 2
        self.x = [i for i in range(0, 315, 32)]
        self.y = [i for i in range(0, 217, 17)]

    def run(self):
        while not self.game_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_end = True
            self.draw()

    def draw(self):
        self.__screen.fill((255, 255, 255))
        for vertical in range(13):
            for gorizontal in range(10):
                if vertical % 2 == 0:
                    pygame.draw.rect(self.__screen, (255, 0, 0), (self.x[gorizontal], self.y[vertical], 30, 15))
                else:
                    pygame.draw.rect(self.__screen, (255, 0, 0), (self.x[gorizontal] - 15, self.y[vertical], 30, 15))
                
        pygame.display.flip()


if __name__ == "__main__":
    app = Bricks()
    app.run()