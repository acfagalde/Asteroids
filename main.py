import pygame # type: ignore
from constants import *
from player import *
from CircleShape import *

def main():
    pygame.init()
    framerate = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while screen != None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        player1.draw(screen)
        player1.update(dt)
        pygame.display.flip()
        dt = framerate.tick(60)/1000




    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
