import pygame

pygame.init()
win_res=(640,480)
red=(236,28,36)
whit_color=(255,255,255)
black_color=(0,0,0)


pygame.display.set_caption("kevin manda #40")
win_surf=pygame.display.set_mode(win_res, pygame.RESIZABLE)




pygame.display.flip()


launched=True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched =False 
        elif event.type== pygame.MOUSEMOTION:
         print("{}".format(event.pos))