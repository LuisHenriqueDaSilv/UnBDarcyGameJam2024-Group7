import pygame

class Island(pygame.sprite.Sprite):
  def __init__(self, type, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.sprites = {}
    
    self.sprites['left'] = pygame.transform.scale(pygame.image.load('assets/Island/left.png'), (128/2.5, 128/2.5))
    self.sprites['mid'] = pygame.transform.scale(pygame.image.load('assets/Island/mid.png'), (128/2.5, 128/2.5))
    self.sprites['right'] = pygame.transform.scale(pygame.image.load('assets/Island/right.png'), (128/2.5, 128/2.5))
    
    self.image = self.sprites[type]
    self.rect = self.image.get_rect()
    self.rect.topleft = x-self.rect.width, y-self.rect.height

  