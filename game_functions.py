import sys
import pygame
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: #move charachter to the right
                ship.moving_right = True
                print("event k right is listening")
        elif event.type == pygame.KEYUP:
            if event.key == key.\