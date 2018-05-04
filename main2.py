import pygame, time, math, random, os, sys, tkinter, string
from pygame.locals import *
from settings import *
from images import *
#initialize the game
pygame.init()
pkmn_settings = Settings()

gameDisplay = pygame.display.set_mode((pkmn_settings.display_width, pkmn_settings.display_height))
area = (pkmn_settings.display_width * pkmn_settings.display_height)

pygame.display.set_caption("Pykemon")


icon = pygame.image.load('finalProject/images/gameIcon.png')       
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

# font & font sizes 
smallfont = pygame.font.SysFont("agencyfb", 25)
medfont = pygame.font.SysFont("agencyfb", 55)
largefont = pygame.font.SysFont("agencyfb", 85)

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
        message_to_screen("HOW TO PLAY", black, -250,size="large")

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
                oak_intro()
            if action == "main":
                game_intro()
            if action =="info":
                information()
            if action =="how to play":
                how_to_play()
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

        # background = pygame.image.load("finalProject/images/blue_bg1.jpg").convert()
        # gameDisplay.blit(background, (0,0))
        # pygame.display.update()

        message_to_screen("PYkemon!",black,-100,size="medium")
        message_to_screen("BATTLE BLUE",blue,-30, size="large")
        message_to_screen("Version 1.0",black,30, size="small")
        message_to_screen("",black,50)
       
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

def oak_intro():
    oak_intro = True
    while oak_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        # pygame.display.update()

        oak = pygame.image.load("finalProject/images/oak.png")
        gameDisplay.blit(oak,(300,70))
        pygame.display.update()
        
        clock.tick(60)

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

        button("play Again", 150,500,150,50, green, light_green, action="play")
        button("controls", 350,500,100,50, yellow, light_yellow, action="controls")
        button("quit", 550,500,100,50, red, light_red, action ="quit")
        button("info", 0,0,100,50, grey, light_grey, action="info")

        pygame.display.update()
        clock.tick(15)

def health_bars(player_health, enemy_health):
    if player_health > 75:
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else:
        player_health_color = red

    if enemy_health > 75:
        enemy_health_color = green
    elif enemy_health > 50:
        enemy_health_color = yellow
    else:
        enemy_health_color = red

    pygame.draw.rect(gameDisplay, player_health_color, (680, 25, player_health, 25))
    pygame.draw.rect(gameDisplay, enemy_health_color, (20, 25, enemy_health, 25))

def gameLoop():
    gameLoop = True
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        


    gameExit = False
    gameOver = False
    FPS = 15

    player_health = 100
    enemy_health = 100

    barrier_width = 50

    # mainTankX = display_width * 0.9
    # mainTankY = display_height * 0.9
    # tankMove = 0
    # currentTurPos = 0
    # changeTur = 0

    # enemyTankX = display_width * 0.1
    # enemyTankY = display_height * 0.9    

    # fire_power = 50
    # power_change = 0

    # xlocation = (pkmn_settings.display_width/2) + random.randint(-0.2*pkmn_settings.display_width, 0.2*pkmn_settings.display_width) 
    # randomHeight = random.randrange(pkmn_settings.display_height*0.1,pkmn_settings.display_height*0.6)

    # # while not gameExit:
        
    # #     if gameOver == True:
    # #         gameDisplay.fill(white)
    # #         message_to_screen("Game Over",red,-50,size="large")
    # #         message_to_screen("Press C to play again or Q to exit",black,50)
    # #         pygame.display.update()
    # #         while gameOver == True:
    # #             for event in pygame.event.get():
    # #                 if event.type == pygame.QUIT:
    # #                     gameExit = True
    # #                     gameOver = False

                    # if event.type == pygame.KEYDOWN:
                    #     if event.key == pygame.K_c:
                    #         gameLoop()
                    #     elif event.key == pygame.K_q:
                            
                    #         gameExit = True
                    #         gameOver = False

        # for event in pygame.event.get():

        #     if event.type == pygame.QUIT:
        #         gameExit = True

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         tankMove = -5
                    
            #     elif event.key == pygame.K_RIGHT:
            #         tankMove = 5
                    
            #     elif event.key == pygame.K_UP:
            #         changeTur = 1
                    
            #     elif event.key == pygame.K_DOWN:
            #         changeTur = -1

            #     elif event.key == pygame.K_p:
            #         pause()

            #     elif event.key == pygame.K_SPACE:
            #         damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,barrier_width,randomHeight,enemyTankX,enemyTankY)
            #         enemy_health -= damage
            #         damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,barrier_width,randomHeight,mainTankX,mainTankY)
            #         player_health -= damage
                    
            #     elif event.key == pygame.K_a:
            #         power_change = -1
            #     elif event.key == pygame.K_d:
            #         power_change = 1

            # elif event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         tankMove = 0

            #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #         changeTur = 0
                    
            #     if event.key == pygame.K_a or event.key == pygame.K_d:
            #         power_change = 0
                
        # mainTankX += tankMove

        # currentTurPos += changeTur

        # if currentTurPos > 8:
        #     currentTurPos = 8
        # elif currentTurPos < 0:
        #     currentTurPos = 0


        # if mainTankX - (tankWidth/2) < xlocation+barrier_width:
        #     mainTankX += 5
            

        # gameDisplay.fill(white)
        # health_bars(player_health,enemy_health)
        # gun = tank(mainTankX,mainTankY,currentTurPos)
        # enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        # fire_power += power_change

        # power(fire_power)

        # barrier(xlocation,randomHeight,barrier_width)
        # gameDisplay.fill(green, rect=[0, display_height-ground_height, display_width, ground_height])
        # pygame.display.update()

        # if player_health < 1:
        #     game_over()
        # elif enemy_health < 1:
        #     you_win()
        # clock.tick(FPS)

    # # pygame.quit()gameExit = False
    # # gameOver = False
    # # FPS = 15

    # player_health = 100
    # enemy_health = 100

    # barrier_width = 50

    # mainTankX = display_width * 0.9
    # mainTankY = display_height * 0.9
    # tankMove = 0
    # currentTurPos = 0
    # changeTur = 0

    # enemyTankX = display_width * 0.1
    # enemyTankY = display_height * 0.9    

    # fire_power = 50
    # power_change = 0

    # xlocation = (pkmn_settings.display_width/2) + random.randint(-0.2*pkmn_settings.display_width, 0.2*pkmn_settings.display_width) 
    # randomHeight = random.randrange(pkmn_settings.display_height*0.1,pkmn_settings.display_height*0.6)

    # # while not gameExit:
        
    # #     if gameOver == True:
    # #         gameDisplay.fill(white)
    # #         message_to_screen("Game Over",red,-50,size="large")
    # #         message_to_screen("Press C to play again or Q to exit",black,50)
    # #         pygame.display.update()
    # #         while gameOver == True:
    # #             for event in pygame.event.get():
    # #                 if event.type == pygame.QUIT:
    # #                     gameExit = True
    # #                     gameOver = False

                    # if event.type == pygame.KEYDOWN:
                    #     if event.key == pygame.K_c:
                    #         gameLoop()
                    #     elif event.key == pygame.K_q:
                            
                    #         gameExit = True
                    #         gameOver = False

        # for event in pygame.event.get():

        #     if event.type == pygame.QUIT:
        #         gameExit = True

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         tankMove = -5
                    
            #     elif event.key == pygame.K_RIGHT:
            #         tankMove = 5
                    
            #     elif event.key == pygame.K_UP:
            #         changeTur = 1
                    
            #     elif event.key == pygame.K_DOWN:
            #         changeTur = -1

            #     elif event.key == pygame.K_p:
            #         pause()

            #     elif event.key == pygame.K_SPACE:
            #         damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,barrier_width,randomHeight,enemyTankX,enemyTankY)
            #         enemy_health -= damage
            #         damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,barrier_width,randomHeight,mainTankX,mainTankY)
            #         player_health -= damage
                    
            #     elif event.key == pygame.K_a:
            #         power_change = -1
            #     elif event.key == pygame.K_d:
            #         power_change = 1

            # elif event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         tankMove = 0

            #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #         changeTur = 0
                    
            #     if event.key == pygame.K_a or event.key == pygame.K_d:
            #         power_change = 0
                
        # mainTankX += tankMove

        # currentTurPos += changeTur

        # if currentTurPos > 8:
        #     currentTurPos = 8
        # elif currentTurPos < 0:
        #     currentTurPos = 0


        # if mainTankX - (tankWidth/2) < xlocation+barrier_width:
        #     mainTankX += 5
            

    
        # health_bars(player_health,enemy_health)
        # gun = tank(mainTankX,mainTankY,currentTurPos)
        # enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        # fire_power += power_change

        # power(fire_power)

        # barrier(xlocation,randomHeight,barrier_width)
        # gameDisplay.fill(green, rect=[0, display_height-ground_height, display_width, ground_height])
        # pygame.display.update()

        # if player_health < 1:
        #     game_over()
        # elif enemy_health < 1:
        #     you_win()
        # clock.tick(FPS)

    pygame.display.update()
    clock.tick(60)
    pygame.quit()
    quit()

game_intro()
gameLoop()

# def pause():
#     paused = True
#     message_to_screen("Paused",black,-100,size="large")
#     message_to_screen("Press C to continue",black, 25, size="medium")
#     message_to_screen("Press Q to quit",black, 75, size="medium")
#     pygame.display.update()
#     while paused:
#         for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     quit()
#         clock.tick(5)