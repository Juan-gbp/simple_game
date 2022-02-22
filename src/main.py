import pygame
from sys import exit

""" initialize all imported pygame modules """
pygame.init()


# Display surface
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')

# simple image
test_surface  = pygame.Surface((100,200))
test_surface.fill('Red')

# regulate frame rate fo the game
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # put surface in another surface
    screen.blit(test_surface, (200,100))
    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60)
