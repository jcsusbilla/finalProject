import pygame, sys, os, math, time, random

class Settings():
    def __init__(self):
        #screen settings
        self.display_width = 1175
        self.display_height = 600
    

#colors
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)
yellow = (200,200,0)
light_yellow = (255,255,0)
green = (34,177,76)
light_green = (0,255,0)
lawn_green = (85,107,87)
blue = (0, 0, 255)
dark_blue = (0,0,139)
grey = (190,190,190)
light_grey = (211,211,211)
dark_grey = (169,169,169)

#map properties
display_height = 600
display_width = 1175
ground_height = 25

#Charizard Speed Properties
player1_grav = 0.8
player1_friction = -0.5
player1_acc = 2

#Pikachu Speed Properties
player2_grav = .8
player2_friction = -0.5
player2_acc = 5

#window settings
pygame.display.set_caption("Pykemon")
icon = pygame.image.load('finalProject/images/gameIcon.png')       
pygame.display.set_icon(icon)