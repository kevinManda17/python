import pygame 

pygame.init()
window_resolution=(800,680)
blank_color=(255,255,255)

pygame.display.set_caption("Kevin Manda #37")
window_surface=pygame.display.set_mode(window_resolution)

naruto_image=pygame.image.load("candela.png")
naruto_image.convert()


launched=True
while launched:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            launched=False


window_surface.fill(blank_color)
window_surface.blit(naruto_image,[10,10])
pygame.display.flip()  