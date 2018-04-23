import pygame, sys, os, time, random, math
from settings import Settings


print("Oak: Hello there!")
print("Oak: Welcome to the world of POKEMON!")
print("Oak: My name is Oak!")
print("Oak: People call me the Pokemon Professor!")
print("Oak: This world is inhabited by creatures called POKEMON!")
print("Oak: For some people, POKEMON are pets. Others use them for battle")
print("Oak: Myself....")
print("Oak: I study POKEMON as a profession.")
player1 = input("First, what is your name?")
print("Right! So your name is " + player1 + "!")
print("This is my grandson. He has been your rival since you were a baby.")
rival = input("Uhhh.. What was his name again?")
print("That's right! I remember now! His name is " + rival + "!")
input("Which POKEMON will you choose as your starter?")
    

play_again = True

while play_again:
    winner = None
    player1_health = 100
    rival_health = 100
    #decides who attacks first
    turn = random.randint(1,2) #determined by speed of current pokemon
    if turn == 1:
        player1_turn = True
        rival_turn = False
        print(player1 + "will attack first")
    else:
        player1_turn = False
        rival_turn = True
        print(rival + "will attack first")


def run_game(): #sets up pygame and creates the settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("PYkemon")


run_game()