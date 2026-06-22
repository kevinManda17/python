import pygame 
"""@kevin Manda"""
win_res=(640,480)
launched=True

pygame.init()
pygame.display.set_caption("kevin Manda #42 on joue du son")
win_surf=pygame.display.set_mode(win_res)
 
avalanche_song=pygame.mixer.Sound("Avalanche.ogg")
ambition_song=pygame.mixer.Sound("01-Ambitions.mp3")
avalanche_song.play()
ambition_song.play()

pygame.display.flip()
while launched :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched=False
        elif event.type == pygame.KEYDOWN:
            if event.key== pygame.K_SPACE:
                ambition_song.stop()
