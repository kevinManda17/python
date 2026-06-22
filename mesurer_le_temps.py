import pygame 

pygame.init()

win_res=(720,680)
blue_color=(132,180,255)
red_color=(255,0,0)
black_color=(0,0,0)
launched=True
clock=pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 2000)


pygame.display.set_caption("kevin Manda")
win_surf=pygame.display.set_mode(win_res)
arial_font=pygame.font.SysFont("arial",36)
pygame.display.flip()



while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched=False
        elif event.type ==pygame.USEREVENT:
            win_surf.fill(black_color)
            texte=arial_font.render(f"{clock.get_fps():2f }.FPS",True,blue_color)
            win_surf.blit(texte,[50,50])
            pygame.display.flip()
        
    clock.tick(60)

    # clock.tick(30) # 30 images par secondes 
 
# print(pygame.time.get_ticks()) # comment recuperer le temps qui s'est ecoule depuis l'initialisaton de pygame


# pygame.time.delay(5000)
# texte=arial_font.render("Bonjour les abonnes ",True,red_color)
# win_surf.blit(texte,[50,50])
# pygame.display.flip()