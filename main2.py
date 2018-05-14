import ctypes
import math
import os
import random
import string
import sys
import time
import tkinter
from tkinter import *

import pygame
from pygame.locals import *

import screens
from images import *
from settings import *

#initialize the game
pygame.init()
pkmn_settings = Settings()

gameDisplay = pygame.display.set_mode((pkmn_settings.display_width, pkmn_settings.display_height))
area = (pkmn_settings.display_width * pkmn_settings.display_height)

pygame.display.set_caption("Pykemon")
icon = pygame.image.load('finalProject/images/gameIcon.png')       
pygame.display.set_icon(icon)

clock = pygame.time.Clock()


white = (255,255,255)
ground_height = 25

# font & font sizes 
smallfont = pygame.font.SysFont("agencyfb", 25)
medfont = pygame.font.SysFont("agencyfb", 55)
largefont = pygame.font.SysFont("agencyfb", 85)

# def pkmn(x,y,speed,hp):
#     x = int(x)
#     y = int(y)
#     speed = 2

# def enemy_pkmn(x,y,speed,hp):
#     x = int(x)
#     y = int(y)
#     speed = 2

class player:
    def __init__(self, velocity, maxJumpRange):
        self.velocity = velocity
        self.maxJumpRange = maxJumpRange
    def setLocation(self, x, y):
        self.x = x
        self.y = y
        self.xVelocity = 0
        self.jumping = False
        self.jumpCounter = 0
        self.falling = True
    def keys(self):
        k = pygame.key.get_pressed()
        if k[K_LEFT]: self.xVelocity =  -self.velocity
        elif k[K_RIGHT]:self.xVelocity = self.velocity
        else: self.xVelocity = 0

        if k[K_UP] and not self.jumping and not self.falling:
            self.jumping = True
            self.jumpCounter = 0 
    def move(self):
        self.x += self.xVelocity
        #check x boundaries
        if self.jumping:
            self.y -= self.velocity
            self.jumpCounter += 1
            if self.jumpCounter == self.maxJumpRange:
                self.jumping = False
                self.falling = True
        elif self.falling:
            if self.y <= pkmn_settings.display_height - 10 and self.y + self.velocity >= pkmn_settings.display_height - 10:
                self.y = pkmn_settings.display_height -10
                self.falling = True
            else:
                self.y += self.velocity
    def draw(self):
        display = pygame.display.get_surface()
        pygame.draw.circle(display, white, (self.x, self.y - 100), 25, 0)
    def do(self):
        self.keys()
        self.move()
        self.draw()
P = player(10,200) #(velocity, maxJumpRange)
P.setLocation(150,500)


def message_box(title,text,style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])

def text_objects(text, color,size = "small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)
   
def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(pkmn_settings.display_width / 2), int(pkmn_settings.display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)

def how_to_play():
    
    htp = True
    while htp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message_to_screen("HOW TO PLAY", black,-250,size="large")
        message_to_screen("Survive as many waves possible by knocking out", blue, -100, size="small")
        message_to_screen("POKEMON with close & far ranged moves. Collect", blue, -60, size="small")
        message_to_screen("EXP from dead POKEMON to evolve your pokemon", blue, -20, size="small")
        message_to_screen("which will increase your HP and strength of your moves!", blue, 20, size="small")
        # message_box("message", "hello", 6)
        button("Main", 350,500,100,50, yellow, light_yellow, action="main")
        
        pygame.display.update()
        clock.tick(15)

def game_controls():
    gcont = True
    while gcont:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Controls",black,-250,size="large")
        message_to_screen("Move PKMN: Left & Right Arrow Keys",dark_blue,-180)
        message_to_screen("Jump: Up Arrow Key",dark_blue,-110)
        message_to_screen("Ranged Attack: / ",dark_blue,-40)
        message_to_screen("Close Attack: . ",dark_blue,30)
        message_to_screen("Pause: P",dark_blue,100)

        button("Main", 350,500,100,50, yellow, light_yellow, action="main")
    
        pygame.display.update()

        clock.tick(15)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "controls":
                game_controls()
            if action == "play":
                gameLoop()
            if action == "main":
                game_intro()
            if action =="info":
                information()
            if action =="how to play":
                how_to_play()
            if action == "next":
                pygame.display.update()
            if action == "choose":
                choose()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)

        # background = pygame.image.load("finalProject/images/bg2.png")
        # gameDisplay.blit(background, (0,0))
        # pygame.display.update()

        message_to_screen("PYkemon!",black,-100,size="medium")
        message_to_screen("BATTLE BLUE",blue,-30, size="large")
        message_to_screen("Version 1.0",black,30, size="small")
       
        button("play", 150,500,100,50, green, light_green, action="play")
        button("controls", 350,500,100,50, yellow, light_yellow, action="controls")
        button("quit", 550,500,100,50, red, light_red, action ="quit")
        button("info", 0,0,100,50, grey, light_grey, action="info")
        button("how to play", 102,0, 100,50, grey, light_grey, action="how to play")
        pygame.display.update()

        clock.tick(15)

def information(): 
    info_ = True
    while info_:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)

        message_to_screen("Borrowed code from:", black, -200)

        button("Main", 350,500,100,50, yellow, light_yellow, action="main")
       
        pygame.display.update()
        clock.tick(60)

def game_over():
    game_over = True
    while game_over:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Game Over",green,-100,size="large")
        message_to_screen("You died :(",black,-30)
        message_to_screen("#sucks2suck", red,-10, size="medium")

        button("Play Again", 150,500,150,50, green, light_green, action="play")
        button("controls", 350,500,100,50, yellow, light_yellow, action="controls")
        button("quit", 550,500,100,50, red, light_red, action ="quit")
        button("info", 0,0,100,50, grey, light_grey, action="info")

        pygame.display.update()
        clock.tick(15)

def choose():
    choose = True
    while choose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        # button("Squirtle", 150,500,100,50, dark_blue, blue, action="")
        # button("Bulbasaur", 350,500,100,50, green, light_green, action="")
        # button("Charmander", 550,500,100,50, red, light_red, action = "")

def you_win():
    win = True
    while win:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("You won!",green,-100,size="large")
        message_to_screen("Congratulations!",black,-30)

        button("play again", 150,500,150,50, green, light_green, action="play")
        button("controls", 350,500,100,50, yellow, light_yellow, action="controls")
        button("quit", 550,500,100,50, red, light_red, action ="quit")
        button("info", 0,0,100,50, grey, light_grey, action="info")

        pygame.display.update()
        clock.tick(15)

def health_bars(player_health):
    if player_health > 75:
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else:
        player_health_color = red

    pygame.draw.rect(gameDisplay, player_health_color, (25, 25, player_health, 25))
  
def wave(level):
    text = smallfont.render("Wave: "+str(level)+"%",True, black)
    gameDisplay.blit(text, [pkmn_settings.display_width/2,0])

def gameLoop():
    player_health = 100

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # gameDisplay.fill(white)

        wavebg = pygame.image.load("finalProject/images/battleBG.png").convert()
        gameDisplay.blit(wavebg, (0,0))
        
        message_to_screen("Wave 1" ,black,-260,size="medium")
        P.do()
        health_bars(player_health)
        # gameDisplay.fill(green, rect=[0, pkmn_settings.display_height-ground_height, pkmn_settings.display_width, ground_height])
        pygame.display.update()
        clock.tick(60)

game_intro()
gameLoop()

def pause():
    paused = True
    message_to_screen("Paused",black,-100,size="large")
    message_to_screen("Press C to continue",black, 25, size="medium")
    message_to_screen("Press Q to quit",black, 75, size="medium")
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        clock.tick(5)
