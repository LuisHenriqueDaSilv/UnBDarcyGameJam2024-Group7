import pygame

class FlyDemon(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.currentStatus = 'idle'
    self.xSpeed = 0;
    self.ySpeed = 0;
    self.life = 100;
    self.sprites = {}
    self.falling = False
    self.sprites['idle'] = []
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_0.png'), (44*1.7, 40*1.7)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_1.png'), (44*1.7, 40*1.7)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_2.png'), (44*1.7, 40*1.7)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_3.png'), (44*1.7, 40*1.7)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_4.png'), (44*1.7, 40*1.7)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_5.png'), (44*1.7, 40*1.7)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_6.png'), (44*1.7, 40*1.7)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_7.png'), (44*1.7, 40*1.7)))

    self.sprites['run'] = []
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_1.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_2.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_3.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_4.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_5.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_6.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_7.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_8.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_9.png'), (44*1.7, 40*1.7)))

    self.sprites['fall'] = []
    self.sprites['fall'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Fall/HeroKnight_Fall_0.png'), (44*1.7, 40*1.7)))
    self.sprites['fall'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Fall/HeroKnight_Fall_1.png'), (44*1.7, 40*1.7)))
    self.sprites['fall'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Fall/HeroKnight_Fall_2.png'), (44*1.7, 40*1.7)))
    self.sprites['fall'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Fall/HeroKnight_Fall_3.png'), (44*1.7, 40*1.7)))


    self.currentSpriteIndex = 0
    self.image = self.sprites[self.currentStatus][self.currentSpriteIndex]

    self.rect = self.image.get_rect()
    self.rect.topleft = 100, 500

  def update(self): 
    currentTypeOfImage = self.currentStatus if not self.falling else 'fall'
    self.currentSpriteIndex = self.currentSpriteIndex +0.2 if self.currentSpriteIndex < len(self.sprites[currentTypeOfImage])-1 else 0;
    self.image = self.sprites[currentTypeOfImage][int(self.currentSpriteIndex)]
    if self.xSpeed < 0:
      self.image = pygame.transform.flip(self.image, True, False)
    if self.ySpeed != 0:
      self.rect.move_ip(0, self.ySpeed)

  def changeStatus(self, newStatus):
    if newStatus == self.currentStatus: return
    self.currentStatus = newStatus
    self.currentSpriteIndex = 0

  def run(self, speed):
    if speed < 0 and self.rect.x < 5: return # Limite  esquerdo
    if speed > 0 and self.rect.x > 600-self.rect.width: return # Limite  direito
    self.xSpeed = speed
    self.rect.move_ip(speed, 0)
    if not self.currentStatus == 'fall': self.changeStatus('run')
  
  def jump(self):
    self.ySpeed = -8
