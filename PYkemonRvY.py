# week 1: idea: PKMN turn based battle - trying to figure out what i should include
# week 2:watching python videos 
# week 3: changed game 
# week 4: created functions for game
# week 5: created screens
# week 6: created characters
# week 7: created attacks, added music

# ***CREDIT FOR CODE:

import ctypes, math, os, random, string, sys, time, tkinter, pygame
from pygame.locals import *
from images import *
from settings import *

#initialize the game
pygame.init() #program
pygame.mixer.init() #music
pkmn_settings = Settings()
gameDisplay = pygame.display.set_mode((pkmn_settings.display_width, pkmn_settings.display_height)) 
vec = pygame.math.Vector2
clock = pygame.time.Clock()

#images/sprites
charizard = pygame.image.load('finalProject/images/charizard.png').convert()
fire = pygame.image.load('finalProject/images/fire.png').convert()
elec = pygame.image.load('finalProject/images/shock.png').convert()
pikachu = pygame.image.load('finalProject/images/pikachu.png').convert()

#sounds
pygame.mixer.music.load("finalProject/sounds/battle_music.mp3")
pygame.mixer.music.set_volume(0.2)

# font & font sizes 
smallfont = pygame.font.SysFont("agencyfb", 25)
medfont = pygame.font.SysFont("agencyfb", 55)
largefont = pygame.font.SysFont("agencyfb", 85)

#player 1 & 2 attributes
#create platforms
class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(grey)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(charizard, (132,134))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.center = (display_width / 2, display_height / 2)
        self.pos = vec(300 / 2, 450)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def update(self): #controls for charizard
        self.acc = vec(0, player1_grav)
        k = pygame.key.get_pressed()
        if k[pygame.K_LEFT]:
            self.acc.x = -player1_acc
        if k[pygame.K_RIGHT]:
            self.acc.x = player1_acc
        if k[pygame.K_UP]:
            self.vel.y = -7

        #equations for motion
        self.acc.x += self.vel.x * player1_friction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        #center of player sets itself to position of player
        self.rect.midbottom = self.pos

        #screen edge boundaries
        if self.rect.right > display_width /2: #right side border for the screen
            self.rect.right = display_width /2
        if self.rect.left < 0: #left side border for the screen
            self.rect.left = 0
    
    def p1_shoot(self):
        flamethrower = Flamethrower(self.rect.right, self.rect.center) #comes out of center right of player 1 rect box
        all_sprites.add(flamethrower)
        flames.add(flamethrower)
class Flamethrower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(fire, (75,24)) #shrinks size of image
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = y
        self.rect.right = x
        self.speedx = 15 #speed of projectile
    def update(self):
        self.rect.x +=self.speedx
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pikachu, (102,102))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.center = (display_width / 2, display_height / 2)
  
        self.pos = vec(975, 450)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def update(self):
        self.acc = vec(0, player2_grav)
        k = pygame.key.get_pressed()
        if k[pygame.K_a]:
            self.acc.x = -player2_acc
        if k[pygame.K_d]:
            self.acc.x = player2_acc
        if k[pygame.K_w]:
            self.rect.x += 1
            p2_hits = pygame.sprite.spritecollide(self,platforms, False)
            self.rect.x -= 1
            if p2_hits:
                self.vel.y = -16

        #equations for motion
        self.acc.x += self.vel.x * player2_friction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        #center of player sets itself to position of player
        self.rect.midbottom = self.pos

        #screen edge boundaries
        if self.rect.left < display_width / 2: #right side border for the screen
            self.rect.left = display_width / 2
        if self.rect.right > 1175: #left side border for the screen
            self.rect.right = 1175
    
    def p2_shoot(self):
        lightning = Lightning(self.rect.left, self.rect.center) #comes out of center right of player 2 rect box
        all_sprites.add(lightning)
        bolt.add(lightning)
class Lightning(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(elec, (75,24))
        self.image.set_colorkey(white) #hides white background behind image
        self.rect = self.image.get_rect()
        self.rect.center = y
        self.rect.left = x
        self.speedx = 20 #speed of lightning bolt
    def update(self):
        self.rect.x -= self.speedx

# on screen functions
def message_box(title,text,style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style) #attributes for a message
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
def text_objects(text, color,size = "small"): #define font attributes
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()    
def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"): #creates parts of the button
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)
def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(pkmn_settings.display_width / 2), int(pkmn_settings.display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)
def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            #defines what clicking each button will do 
            if action =="controls":
                game_controls()
            if action =="play":
                gameLoop()
            if action =="info":
                information()
            if action =="how to play":
                how_to_play()
            if action =="main":
                hello()
            if action == "enter":
                game_intro()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)
def health_bars(player_health, player2_health):
    #player 1 health bar
    if player_health > 75:
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else:
        player_health_color = red
    
    #player 2 health bar
    if player2_health > 75:
        player2_health_color = green
    elif player2_health > 50:
        player2_health_color = yellow
    else:
        player2_health_color = red

    pygame.draw.rect(gameDisplay, player_health_color, (25, 65, player_health, 25))
    pygame.draw.rect(gameDisplay, player2_health_color, (1025, 65, player2_health, 25))

# screens
def how_to_play():
    
    htp = True
    while htp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message_to_screen("HOW TO PLAY", black,-250,size="large")
        message_to_screen("Charizrd can fly but is slow  -  Pikachu can jump but is fast ", blue, -100, size="small")
        message_to_screen("Charizard has more HP but a weaker & slower attack  -  Pikachu has less HP but a stronger & faster attack ", blue, -60, size="small")
        message_to_screen("Jump to dodge projectiles", blue, -20, size="small")
        message_to_screen("FIGHT", red, 40, size="medium")
       
        button("Main", 540,500,100,50, yellow, light_yellow, action="main")
        
        pygame.display.update()
        clock.tick(15)
def game_controls():
    controls = True
    while controls:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Controls",black,-250,size="large")
        message_to_screen("Move PKMN: Left & Right Arrow  / W & D",dark_blue,-180)
        message_to_screen("Jump: Up Arrow Key, W ",dark_blue,-110)
        message_to_screen("Attack: Period, f ",dark_blue,-40)
        message_to_screen("Pause: SPACE",dark_blue,30)
    
        button("Main", 540,500,100,50, yellow, light_yellow, action="enter")
    
        pygame.display.update()
        clock.tick(5)
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        
        gameDisplay.fill(white)

        message_to_screen("PYkemon!",black,-210,size="medium")
        message_to_screen("BATTLE ARENA",blue,-140, size="large")
        message_to_screen("RED VS YELLOW",black,-70, size="medium")
       
        button("play", 540,292,100,50, green, light_green, action="play")
        button("controls", 540,344,100,50, yellow, light_yellow, action="controls")
        button("quit", 540,500,100,50, red, light_red, action ="quit")
        button("info", 540,396,100,50, grey, light_grey, action="info")
        button("how to play", 540, 448, 100,50, grey, light_grey, action="how to play")
        pygame.display.update()

        clock.tick(5)
def information(): 
    info_ = True
    while info_:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)

        message_to_screen("Thanks to:", black, -200)
        message_to_screen("Bucky Roberts, Code PyLet, KidsCanCode, Roblox, Pokemon, Mr. Cozort", blue, -150)

        button("Main", 540,500,100,50, yellow, light_yellow, action="main")
       
        pygame.display.update()
        clock.tick(60)
def p1_wins():
    pygame.mixer.music.stop()
    win = True
    while win:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        gameDisplay.blit(oof, (200,-25))

        message_to_screen("Player 1 Wins!",green,-100,size="large")
        message_to_screen("sucks2suck @ pikachu!",white,-30)

        button("play", 540, 396, 100, 50, green, light_green, action="play")
        button("controls", 540, 448, 100, 50, yellow, light_yellow, action="controls")
        button("quit", 540, 500, 100, 50, red, light_red, action ="quit")
    
        pygame.display.update()
        clock.tick(15)
def p2_wins():
    pygame.mixer.music.stop()
    win = True
    while win:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        gameDisplay.blit(oof, (200,-25))
        
        message_to_screen("Player 2 Wins!",green,-100,size="large")
        message_to_screen("take the L @ charizard!",white,-30)

        button("play", 540, 396, 100, 50, green, light_green, action="play")
        button("controls", 540, 448, 100, 50, yellow, light_yellow, action="controls")
        button("quit", 540, 500, 100, 50, red, light_red, action ="quit")

        pygame.display.update()
        clock.tick(15)
def hello():
    hi = True
    while hi:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)

        button("enter", display_width / 2 - 50, display_height / 2, 100, 50, green, light_green, action="enter")

        pygame.display.update()
        clock.tick(15)
def pause():
    paused = True
    gameDisplay.fill(black, rect=[345.5, 150, 475, 290])
    message_to_screen("Paused",white,-100,size="large")
    message_to_screen("Press C to continue",white, 25, size="medium")
    message_to_screen("Press M for menu screen ",white, 75, size="medium")    
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c: #continue game
                        paused = False
                    elif event.key == pygame.K_m: #return to main menu
                        pygame.mixer.music.stop() #stops battle music
                        game_intro()   
                        
        clock.tick(5)
def gameLoop():

    pygame.mixer.music.play(loops=-1) # play and make background music continuous
    
    #define player hitpoints
    player1_health = 150
    player2_health = 100

    game = True
    #game loop
    while game: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PERIOD:
                    player1.p1_shoot()
                elif event.type == pygame.K_UP:
                    player1.jump()
                elif event.type == pygame.K_w:
                    player2.jump()
                elif event.key == pygame.K_SPACE:
                    pause()
                elif event.key == pygame.K_f:
                    player2.p2_shoot()
        #update screen
        all_sprites.update()       

        #check to see if bullet hits other player
        p1_collide = pygame.sprite.spritecollide(player1, platforms, False)
        if p1_collide: #allows charizard to fly / endless jumping
            player1.pos.y = p1_collide[0].rect.top + 2
            player1.vel.y = 0

        if player2.vel.y > 0: #pikachu can jump through and land on platforms
            p2_collide = pygame.sprite.spritecollide(player2, platforms, False)
            if p2_collide:
                player2.pos.y = p2_collide[0].rect.top + 2
                player2.vel.y = 0

        #check to see if attack hits other player
        p1hits = pygame.sprite.spritecollide(player2, flames, True, False)
        if p1hits: 
            player2_health -= 12 #player1 attack damage
        p2hits = pygame.sprite.spritecollide(player1,bolt, True, False)
        if p2hits:
            player1_health -= 17 #player 2 attack damage

        #draws battle background
        wavebg = pygame.image.load("finalProject/images/battleBG.png").convert()
        gameDisplay.blit(wavebg, (0,0))

        #draws all sprites to the screen
        all_sprites.draw(gameDisplay) 
        
        #so player doesnt teleport to top of platform when jumping
        if player2.vel.y > 0:
            p2_thru = pygame.sprite.spritecollide(player2, platforms, False)
            if p2_thru:
                player2.pos.y = p2_thru[0].rect.top
                player2.vel.y = 0

        #draw POKEMON names
        message_to_screen("CHARIZARD                                                                                        ", red, -268, size="medium")
        message_to_screen("                                                                                        PIKACHU", yellow, -268, size="medium")
        
        #draw health bars
        health_bars(player1_health, player2_health)

        #flip the display after drawing everything
        pygame.display.flip()
        clock.tick(300)

        #decides the game outcome
        if player1_health < 0:
            p2_wins()
        if player2_health < 0:
            p1_wins()
        clock.tick(300)

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
flames = pygame.sprite.Group()
bolt = pygame.sprite.Group()

player1 = Player1()
all_sprites.add(player1)
player2 = Player2()
all_sprites.add(player2)

p1 = Ground(0, display_height - 40, display_width, 40)
p2 = Platform(display_width / 2 + 230 , display_height - 175, 150, 20)
p3 = Platform(display_width / 2 + 30,display_height - 320 , 150, 20)
p4 = Platform(display_width / 2 + 430, display_height - 320, 150, 20)
all_sprites.add(p2)
all_sprites.add(p1)
all_sprites.add(p3)
all_sprites.add(p4)
platforms.add(p1)
platforms.add(p2)
platforms.add(p3)
platforms.add(p4)

game_intro()