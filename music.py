import pygame 
import tkinter as tkr

pygame.init()

# ZOMBIE CODE ; screen = pygame.display.set_mode([800, 800])

#setup windows python

#Window Parameters
window = tkr.Tk()

screen = pygame.display.set_mode([800, 800])

tkr.Label(pygame, text="Allah will punish you", height = 10, width = 10, bg="black", fg="white")



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    screen.fill((255, 255, 255)) 
    
    
    
    
    pygame.display.flip()
    
    
pygame.quite()