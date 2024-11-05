import pygame

class DemonFly(pygame.sprite.Sprite):
  def __init__(self, y, xa, xb):
    pygame.sprite.Sprite.__init__(self)
    self.currentStatus = 'idle'
    self.sprites = {}
    self.falling = False
    self.xSpeed = 0
    self.xa = xa
    self.xb = xb
    self.y = y
    self.sprites['idle'] = []
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Idle/Demon_Fly_Idle_0.png'), (79, 69)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Idle/Demon_Fly_Idle_1.png'), (79, 69)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Idle/Demon_Fly_Idle_2.png'), (79, 69)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Idle/Demon_Fly_Idle_3.png'), (79, 69)))

    self.sprites['hurt'] = []
    self.sprites['hurt'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Hurt/Demon_Fly_Hurt_0.png'), (79, 69)))
    self.sprites['hurt'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Hurt/Demon_Fly_Hurt_1.png'), (79, 69)))
    self.sprites['hurt'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Hurt/Demon_Fly_Hurt_2.png'), (79, 69)))
    self.sprites['hurt'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Hurt/Demon_Fly_Hurt_3.png'), (79, 69)))

    self.sprites['flying'] = []
    self.sprites['flying'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Flying/Demon_Fly_Flying_0.png'), (79, 69)))
    self.sprites['flying'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Flying/Demon_Fly_Flying_1.png'), (79, 69)))
    self.sprites['flying'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Flying/Demon_Fly_Flying_2.png'), (79, 69)))
    self.sprites['flying'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Flying/Demon_Fly_Flying_3.png'), (79, 69)))

    self.sprites['death'] = []
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Death/Demon_Fly_Death_0.png'), (79, 69)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Death/Demon_Fly_Death_1.png'), (79, 69)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Death/Demon_Fly_Death_2.png'), (79, 69)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Death/Demon_Fly_Death_3.png'), (79, 69)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Death/Demon_Fly_Death_4.png'), (79, 69)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Death/Demon_Fly_Death_5.png'), (79, 69)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Death/Demon_Fly_Death_6.png'), (79, 69)))

    self.sprites['attack'] = []
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Attack/Demon_Fly_Attack_0.png'), (79, 69)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Attack/Demon_Fly_Attack_1.png'), (79, 69)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Attack/Demon_Fly_Attack_2.png'), (79, 69)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Attack/Demon_Fly_Attack_3.png'), (79, 69)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Attack/Demon_Fly_Attack_4.png'), (79, 69)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Attack/Demon_Fly_Attack_5.png'), (79, 69)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Attack/Demon_Fly_Attack_6.png'), (79, 69)))

    self.currentSpriteIndex = 0
    self.image = self.sprites[self.currentStatus][self.currentSpriteIndex]

    self.rect = self.image.get_rect()
    # self.rect.topleft = 100, 500
    self.rect.topleft = xa, y


  def update(self): 
    currentTypeOfImage = self.currentStatus if not self.falling else 'fall'
    self.currentSpriteIndex = self.currentSpriteIndex +0.2 if self.currentSpriteIndex < len(self.sprites[currentTypeOfImage])-1 else 0;
    self.image = self.sprites[currentTypeOfImage][int(self.currentSpriteIndex)]
    self.move()
    if self.xSpeed > 0:
      self.image = pygame.transform.flip(self.image, True, False)

  def changeStatus(self, newStatus):
    if newStatus == self.currentStatus: return
    self.currentStatus = newStatus
    self.currentSpriteIndex = 0
  
  def move(self):
    if self.rect.x <= self.xa: 
      self.xSpeed = 1
    elif self.rect.x >= self.xb:
      self.xSpeed = -1
    
    self.rect.move_ip(self.xSpeed, 0)
