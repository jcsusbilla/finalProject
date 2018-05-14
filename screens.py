# def oak_intro():
#     oak_intro = True
#     while oak_intro:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()

#         gameDisplay.fill(white)
        
#         oak_bg = pygame.image.load("finalProject/images/oak_bg.jpg").convert()
#         gameDisplay.blit(oak_bg, (0,0))
#         # pygame.display.update()

#         oak = pygame.image.load("finalProject/images/oak.png")
#         gameDisplay.blit(oak,(207,65))
#         # button("next", 700,550,100,50, dark_blue, blue, action ="next")

#         pygame.display.update()
        
#         clock.tick(60)