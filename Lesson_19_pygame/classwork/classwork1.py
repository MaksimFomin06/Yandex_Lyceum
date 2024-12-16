import pygame

class Dz1:
    def __init__(self, screen_width: int, screen_height: int, n: int) -> None:
        pygame.init()
        self.width: int = screen_width
        self.height: int = screen_height
        self.n = n
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
    try:
        input_data = input().strip()
        size, n = map(int, input_data.split())
        dz1 = Dz1(size, size, n)
        dz1.run()
    except ValueError:
        print("Неправильный формат ввода")
        exit()

if __name__ == "__main__":
    main()