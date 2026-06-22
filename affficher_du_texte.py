import pygame

pygame.init()
win_res=(640,480)
red=(236,28,36)

pygame.display.set_caption("kevin manda #39")
win_surf=pygame.display.set_mode(win_res)


arial_font=pygame.font.SysFont("arial",50)
hello_texte_surface=arial_font.render("Hello kevin",False, red)

win_surf.blit(hello_texte_surface,[10,10])
pygame.display.flip()
# print(pygame.font.get_fonts())

launched=True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched =False 