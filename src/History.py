import pygame

class History():
  def __init__(self):
    self.step = 0
  
  def update(self, screen):
    if self.step == 0:
      well = pygame.transform.scale(pygame.image.load('assets/history/scene1/Well.png'), (480/3, 480/3))
      lantern = pygame.transform.scale(pygame.image.load('assets/history/scene1/Street_Lantern.png'), (128/2.5, 128/2.5))
      barrel = pygame.transform.scale(pygame.image.load('assets/history/scene1/Wooden_Barrel.png'), (128/2.5, 128/2.5))
      cart = pygame.transform.scale(pygame.image.load('assets/history/scene1/Cart.png'), (128/2.5, 128/2.5))

      screen.blit(well, (0,0))
      pygame.display.flip()
      return True