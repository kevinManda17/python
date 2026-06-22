import pygame 


pygame.init()

window_resolution=(640,480)       #definition de la resolution de la fenetre pygame
blue_color=(97, 190 , 110)        #definition du tuple pour le changement du couleur en RGB 
black_color=(0,0,0)

pygame.display.set_caption("KEVEN #36")   

window_surface=pygame.display.set_mode(window_resolution)
window_surface.fill(blue_color)

rect_form=pygame.Rect(10,10,150,65)
pygame.draw.circle(window_surface, black_color,[300,250],200)

pygame.display.flip()  #Aide au changement  de couleur 


# boucle infinie pour la fenetre pygame 
launched=True 
while launched :
    for event in pygame.event.get():
        if event.type== pygame.QUIT :
            launched= False