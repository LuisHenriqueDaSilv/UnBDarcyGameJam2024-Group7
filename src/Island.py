import pygame

class Island(pygame.sprite.Sprite):
  def __init__(self, type, x, y):
    self.sprites = {}
    
    self.sprites['left'] = pygame.transform.scale(pygame.image.load('assets/Island/left.png'), (123, 100))
    self.sprites['mid'] = pygame.transform.scale(pygame.image.load('assets/Island/mid.png'), (128/2.5, 128/2.5))
    self.sprites['right'] = pygame.transform.scale(pygame.image.load('assets/Island/right.png'), (100, 100))
    
    self.allSprites = pygame.sprite.Group()

    self.image = self.sprites[type]
    self.rect = self.image.get_rect()
    self.rect.topleft = x, y - self.rect.height

    pygame.sprite.Sprite.__init__(self)
  