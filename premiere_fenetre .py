import pygame 

pygame.init()
window_surface=pygame.display.set_mode((640, 480))

pygame.display.set_caption("KEVEN")

print(pygame.get_sdl_version())
launched=True 
while launched :
    for event in pygame.event.get():
        if event.type== pygame.QUIT :
            launched= False
