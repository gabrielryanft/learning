import pygame
pygame.init() #para iniciar o pygame

print('Oi')
pygame.mixer.music.load("cursoemvideo/exerciciospython/ex021/ribe.mp3")
pygame.mixer.music.play()
pygame.event.wait()
pygame.mixer.music.set_volume(0.01) #volume. ñ entendi como funciona mas eu acho que é de 0(baixo) até 1(alto paca*****)
while pygame.mixer.music.get_busy():
    continue
"""
    eu usei no terminal o comando : pip install pygame
    daí ele instalou e eu usei.
"""