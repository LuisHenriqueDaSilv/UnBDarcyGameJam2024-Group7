import pygame

from src.Player import Player
from src.Background import Background
from src.createWorld import createWorld
from src.createEnemies import createEnemies
from src.lifeBar import LifeBar
from settings import *

from settings import SCREEN_HEIGHT, SCREEN_WIDTH
pygame.init()
pygame.display.set_caption("UnB Darcy Game Jam - Grupo 07")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
hitSound = pygame.mixer.Sound('song/hitSound.wav')

mostrar_frase = True
inicio_jogo = False
musica_de_fundo_tocando = False


allSprites = pygame.sprite.Group()
floorGroup = pygame.sprite.Group()
enemiesGroup = pygame.sprite.Group()
backgroundGroup = pygame.sprite.Group()
lifebarGroup = pygame.sprite.Group()

dirtBaseBackground = Background(0, 'dirt')
florestBackbackground = Background(0, 'florest')
skyBackbackground = Background(0, 'sky')
for i in range(3):
  backgroundGroup.add(Background(-i*dirtBaseBackground.rect.height, 'dirt'))

backgroundGroup.add(Background(-2*SCREEN_HEIGHT-florestBackbackground.rect.height, 'florest'))
skyInit = -2*SCREEN_HEIGHT-florestBackbackground.rect.height
backgroundGroup.add(Background(skyInit-skyBackbackground.rect.height, 'sky'))

player = Player()
allSprites.add(player)
lifebar = LifeBar()
lifebarGroup.add(lifebar)

createWorld(floorGroup)
createEnemies(enemiesGroup)

pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.load('song/background-sound.mpeg')
pygame.mixer.music.play(-1)  # Toca a música em loop
musica_de_fundo_tocando = True

running = True
while running:

  clock.tick(FPS) 
  screen.fill((0, 0, 0))

  playerCollidesWithFloor = pygame.sprite.spritecollide(player, floorGroup, False)
  leftCollide = False
  rightCollide = False
  bottomCollide = False
  topCollide = False
  for collide in playerCollidesWithFloor:
    playerFoot = player.rect.height+player.rect.y
    playerHead = player.rect.y
    blockBottom = collide.rect.y + collide.rect.height 
    playerRight = player.rect.x+player.rect.height
    blockLeft = collide.rect.x + collide.rect.width
    if collide.rect.y-15 < playerFoot and collide.rect.y+15 > playerFoot:
      bottomCollide = True
    elif playerHead+15 > blockBottom and playerHead -15 < blockBottom:
      topCollide = True
    elif playerRight+15 > collide.rect.x and playerRight-15 < collide.rect.x: 
      rightCollide = True
    elif blockLeft +15 > player.rect.x and blockLeft-15 < player.rect.x:
      leftCollide = True
  player.bottomCollide = bottomCollide
  player.topCollide = topCollide
  player.leftCollide = leftCollide
  player.rightCollide = rightCollide
    
  playerCollidesWithEnemies = pygame.sprite.spritecollide(player, enemiesGroup, False)
  for enemie in playerCollidesWithEnemies: 
    if player.currentStatus == 'attack':
      if player.lastMove > 0: 
        enemie.hit(15, 0)
      else:
        enemie.hit(15, 1)
    elif enemie.currentStatus == 'attack':
      player.hit(enemie.damage)

  if inicio_jogo:
      # Verifica colisões com inimigos
      playerCollidesWithEnemies = pygame.sprite.spritecollide(player, enemiesGroup, False)
      for enemie in playerCollidesWithEnemies:
          if player.currentStatus == 'attack':
              if player.lastMove > 0:
                  enemie.hit(15, 0)
              else:
                  enemie.hit(15, 1)
          elif enemie.currentStatus == 'attack':
              player.hit(enemie.damage)

      # Movimentos e ataques do jogador
      key = pygame.key.get_pressed()
      if key[pygame.K_a] and player.bottomCollide and not player.currentStatus == 'attack' and not player.currentStatus == 'death':
          player.run(-5)
      elif key[pygame.K_d] and player.bottomCollide and not player.currentStatus == 'attack' and not player.currentStatus == 'death':
          player.run(5)
      elif key[pygame.K_f] and not player.currentStatus == 'death':
          player.attack()
          hitSound.set_volume(1)
          hitSound.play()
      elif key[pygame.K_e] and player.currentStatus != "attack" and not player.currentStatus == 'death' and player.currentStatus != "block":
        player.defense()
      elif player.bottomCollide and not player.currentStatus == 'attack' and not player.currentStatus == 'death' and player.currentStatus != 'block':
          player.xSpeed = 0
          player.changeStatus('idle')

      if key[pygame.K_SPACE] and not player.currentStatus == 'death':
          player.jump()
  

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
              # Ao pressionar Enter, a música toca e o jogo começa
              mostrar_frase = False
              inicio_jogo = True


  backgroundGroup.draw(screen)
  allSprites.update()
  allSprites.draw(screen)

  if inicio_jogo:
    for enemie in enemiesGroup:
      enemie.update(player.rect.y, player.ySpeed, player)
  
  for floor in floorGroup: 
    floor.update(player.rect.y, player.ySpeed)
  floorGroup.draw(screen)
  for background in backgroundGroup:
    background.update(player.rect.y, player.ySpeed)

  enemiesGroup.draw(screen)
  pygame.draw.rect(screen, (255, 0, 0), (17, 15.5, 161.5 * player.life / 100, 30))
  lifebarGroup.draw(screen)
  lifebarGroup.update()  

  if mostrar_frase:
      fonte = pygame.font.SysFont('arial', 40, True, False)
      mensagem = 'press enter'
      texto_formatado = fonte.render(mensagem, False, (255, 255, 255))
      screen.blit(texto_formatado, (210, 390))

  pygame.display.flip()

pygame.quit()