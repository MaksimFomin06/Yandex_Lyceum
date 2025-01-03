import pygame


class Counter:
    def __init__(self, screen_width = 200, screen_height = 200):
        pygame.init()
        self.__width = screen_width
        self.__height = screen_height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.game_end = False
        
        self.count = 0

    def run(self):
        self.draw()
        self.check_events()
    
    def check_events(self):
        while not self.game_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_end = True
                elif event.type == pygame.WINDOWMINIMIZED:
                    self.count += 1
                    self.draw()
            pygame.display.flip()

    def draw(self):
        self.__screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render(f"{self.count}", True, (255, 0, 0))
        text_rect = text.get_rect(center=(100, 100))
        self.__screen.blit(text, text_rect)


def main():
    app = Counter()
    app.run()


if __name__ == "__main__":
    main()