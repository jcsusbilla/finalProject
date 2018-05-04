import sys, pygame, math
from settings import *
pkmn_settings = Settings()
black = (0,0,0)

def update_mouse():
    p = pygame.mous.get_pos()
    return str(p)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(pkmn_settings, text, screen):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (pkmn_settings.screen_width/2, pkmn_settings.screen_height/2)
    screen.blit(TextSurf, TextRect)

def check_events(pkmn_settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # elif event.type == pygame.KEYDOWN:
        #     check_keydown_events(event, ai_settings, screen, ship, bullets)


def update_screen(pkmn_settings, screen):
    #redraws the loop
    screen.fill(pkmn_settings.bg_color)
    pygame.display.flip()
