import pygame #type:ignore
import buttons as bt
import colors as c

pygame.init()

class Chemistry_Lab_Simulator:
    def __init__(self):
        self.w, self.h = 800, 450
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Genetic Algorithm Program 2: Evolving Flowers")
        self.clock = pygame.time.Clock()
        self.tiny_font = pygame.font.Font(None, 25)
        self.big_font = pygame.font.Font(None, 48)
        self.medium_font = pygame.font.Font(None, 38)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.fill(c.WHITE)
            pygame.display.update()
            self.clock.tick(60)

x = Chemistry_Lab_Simulator()
x.run()