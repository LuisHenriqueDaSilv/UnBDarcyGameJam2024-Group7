import pygame
from .Island import Island
from .Killer import Killer
from .Player import Player
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

class History():
  def __init__(self, screen):
    self.screen = screen
    self.step = 1
    self.subStep = 0

    self.well = pygame.transform.scale(pygame.image.load('assets/history/scene1/Well.png'), (480/3, 480/3))
    self.lantern = pygame.transform.scale(pygame.image.load('assets/history/scene1/Street_Lantern.png'), (480/2.5, 480/2))
    self.barrel = pygame.transform.scale(pygame.image.load('assets/history/scene1/Wooden_Barrel.png'), (128/2.5, 128/2.5))
    self.cart = pygame.transform.scale(pygame.image.load('assets/history/scene1/Cart.png'), (256/2, 256/2))
    self.midIsland = pygame.transform.scale(pygame.image.load('assets/Island/mid.png'), (128/2.5, 128/2.5))
    self.dirt = pygame.transform.scale(pygame.image.load('assets/Island/ground.png'), (128/2.5, 128/2.5))
    self.sky = pygame.transform.scale(pygame.image.load('assets/skyBackground.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
    self.dialogueBlock = pygame.transform.scale(pygame.image.load('assets/dialogueBlock.svg'), (1214/2, 321/2))
    

    killerBase = Killer(0, 0)
    playerBase= Player(0,0)
    self.personsGroup = pygame.sprite.Group()
    self.killer = Killer(-100, SCREEN_HEIGHT/1.5-killerBase.rect.height)
    self.player = Player(270, SCREEN_HEIGHT/1.5-playerBase.rect.height, True)
    self.personsGroup.add(self.killer)
    self.personsGroup.add(self.player)

  def scene1(self, paused =False):
    pygame.event.get()

    midIsland = Island('mid', 0, 0)
    numberOfIslands = SCREEN_WIDTH/midIsland.rect.width
    self.screen.blit(self.sky, (0,0))

    for i in range (int(numberOfIslands)+2):
      for j in range (int(numberOfIslands)+2):
        self.screen.blit(self.midIsland if j == 0 else self.dirt, (i*120/2.5, SCREEN_HEIGHT/1.5+j*120/2.5))

    self.screen.blit(self.well, (SCREEN_WIDTH-200,SCREEN_HEIGHT/1.5-self.well.get_rect().height))
    self.screen.blit(self.lantern, (SCREEN_WIDTH-self.lantern.get_rect().width, SCREEN_HEIGHT/1.5-self.lantern.get_rect().height))
    self.screen.blit(self.barrel, (SCREEN_WIDTH-self.barrel.get_rect().width, SCREEN_HEIGHT/1.5-self.barrel.get_rect().height))
    self.screen.blit(self.cart, (0, SCREEN_HEIGHT/1.5-self.cart.get_rect().height))
    if not paused:
      if self.subStep == 0:
        if self.killer.rect.x<200:
          self.killer.currentStatus = "run"
          self.killer.rect.move_ip(3, 0)
        else:
          self.killer.currentStatus = "idle"
          self.subStep += 1
      if self.subStep == 1:
        self.screen.blit(self.dialogueBlock, (0, SCREEN_HEIGHT-200))
        fonte = pygame.font.SysFont('arial', 20, True, False)
        mensagem = 'Sabia que isso terminaria assim,'
        texto_formatado = fonte.render(mensagem, False, (48, 47, 42))
        self.screen.blit(texto_formatado, (100, SCREEN_HEIGHT-140))
        mensagem = 'mais cedo ou mais tarde'
        texto_formatado = fonte.render(mensagem, False, (48, 47, 42))
        self.screen.blit(texto_formatado, (100, SCREEN_HEIGHT-110))
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      if self.subStep == 2:
        self.screen.blit(self.dialogueBlock, (0, SCREEN_HEIGHT-200))
        fonte = pygame.font.SysFont('arial', 20, True, False)
        mensagem = 'Então termine logo.'
        texto_formatado = fonte.render(mensagem, False, (48, 47, 42))
        self.screen.blit(texto_formatado, (100, SCREEN_HEIGHT-140))
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      if self.subStep == 3:
        self.screen.blit(self.dialogueBlock, (0, SCREEN_HEIGHT-200))
        fonte = pygame.font.SysFont('arial', 20, True, False)
        mensagem = 'Com honra'
        texto_formatado = fonte.render(mensagem, False, (48, 47, 42))
        self.screen.blit(texto_formatado, (100, SCREEN_HEIGHT-140))
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      if self.subStep == 4:
        if self.killer.rect.x<240:
          self.killer.currentStatus = "run"
          self.killer.rect.move_ip(3, 0)
        else:
          self.subStep += 1
          self.killer.currentSpriteIndex = 0
          self.killer.currentStatus = "attack"
      if self.subStep == 5:
        if int(self.killer.currentSpriteIndex) >= 3:
          self.killer.currentStatus = "idle"
          self.subStep+=1
      if self.subStep == 6:
        return True

    self.personsGroup.update()
    self.personsGroup.draw(self.screen)
    if not paused: pygame.display.flip()
    return False

  def update(self,paused =False):

    if self.step == 1:
      return self.scene1(paused)
    return False