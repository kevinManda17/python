import pygame 
import time 

pygame.init()
win_res=(640,480)
black=(0,0,0)
red=(255,0,0)
blue=(0,75,255)
i=0

pygame.display.set_caption("kevin Manda #38")
win_surf=pygame.display.set_mode(win_res)

myrect=pygame.Rect(10,100,25,25)
myblock=pygame.Rect(600,50,20,300)
pygame.draw.rect(win_surf,red,myrect)
pygame.draw.rect(win_surf,blue,myblock)
pygame.display.flip()


launched= True 
while launched:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            launched=False


while not  myrect.colliderect(myblock) is  True :
    time.sleep(.010)
    win_surf.fill(black)
    myrect.x +=1
    pygame.draw.rect(win_surf,red,myrect)
    pygame.draw.rect(win_surf,blue,myblock)
    pygame.display.flip()
