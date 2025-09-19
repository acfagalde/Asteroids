import pygame # type: ignore
from constants import *
from player import *
from CircleShape import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    framerate = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)


    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    basefield = AsteroidField()

    while screen != None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        for item in drawable:
            item.draw(screen)
        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.collisions(player1) is True:
                print("Game over!")
                exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collisions(shot) is True:
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        dt = framerate.tick(60)/1000




    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
