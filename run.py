import pygame
import random

from src.Player import Player
from src.Background import Background
from src.createWorld import createWorld
from src.createEnemies import createEnemies
from src.lifeBar import LifeBar
from src.Cutscene import History
from settings import *

from settings import SCREEN_HEIGHT, SCREEN_WIDTH
pygame.init()
pygame.display.set_caption("UnB Darcy Game Jam - Grupo 07")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
hitSound = pygame.mixer.Sound('song/hitSound.wav')

ambient_sounds = [
    pygame.mixer.Sound('song/AmbientSound/AmbientSound 1.wav'),
    pygame.mixer.Sound('song/AmbientSound/AmbientSound 2.wav'),
    pygame.mixer.Sound('song/AmbientSound/AmbientSound 3.wav'),
    pygame.mixer.Sound('song/AmbientSound/AmbientSound 4.wav'),
    pygame.mixer.Sound('song/AmbientSound/AmbientSound 5.wav'),
    pygame.mixer.Sound('song/AmbientSound/AmbientSound 6.wav'),
    pygame.mixer.Sound('song/AmbientSound/AmbientSound 7.wav'),
    pygame.mixer.Sound('song/AmbientSound/AmbientSound 8.wav'),
]

for sound in ambient_sounds:
    sound.set_volume(0.7)


history = History(screen)

restart = True
def main():
  next_ambient_sound_time = pygame.time.get_ticks() + random.randint(30000, 45000)
  mostrar_frase = True
  inicio_jogo = False

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
  backgroundGroup.add(Background(skyInit-2*skyBackbackground.rect.height, 'sky'))
  backgroundGroup.add(Background(skyInit-3*skyBackbackground.rect.height, 'sky'))
  backgroundGroup.add(Background(skyInit-4*skyBackbackground.rect.height, 'sky'))
  backgroundGroup.add(Background(skyInit-5*skyBackbackground.rect.height, 'sky'))


  game_over_image = pygame.image.load('assets/gameOver.png')
  game_over_image = pygame.transform.scale(game_over_image, (400, 390))

  player = Player(200, SCREEN_HEIGHT-150)
  allSprites.add(player)
  lifebar = LifeBar()
  lifebarGroup.add(lifebar)

  createWorld(floorGroup)
  createEnemies(enemiesGroup)

  gameOverSound = pygame.mixer.Sound('song/gameOver1.wav')
  pygame.mixer.music.set_volume(0.5) #Adicionar dps
  pygame.mixer.music.load('song/background-sound.mpeg')
  pygame.mixer.music.play(-1)  # Toca a música em loop

  running = True
  while running:
    clock.tick(FPS) 

    if not inicio_jogo:    
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
          elif event.type == pygame.KEYDOWN:
              if event.key == pygame.K_RETURN:
                mostrar_frase = False
                inicio_jogo = True

    freeToPlay = history.update(not inicio_jogo)
    print(freeToPlay)

    if not inicio_jogo:       
      fonte = pygame.font.SysFont('arial', 40, True, False)
      mensagem = 'press enter'
      texto_formatado = fonte.render(mensagem, False, (255, 255, 255))
      screen.blit(texto_formatado, (210, 390))   
      pygame.display.flip()

    if not freeToPlay: continue

    screen.fill((0, 0, 0))
    current_time = pygame.time.get_ticks()
    if current_time >= next_ambient_sound_time:
      print("Random")
      random.choice(ambient_sounds).play()
      next_ambient_sound_time = current_time + random.randint(30000, 45000)

    if player.dead:  # Se o jogador morreu, exibe a tela de Game Over
        backgroundGroup.draw(screen)
        screen.blit(game_over_image, (90, 240))
        pygame.display.flip()

        if not pygame.mixer.get_busy():  # Verifica se a música de Game Over não está tocando
            gameOverSound.play()  # Toca o som de Game Over apenas uma vez

        # Espera até que o jogador pressione uma tecla para sair ou reiniciar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                restart = False
            elif event.type == pygame.KEYDOWN:
                restart = True
                running = False
                player.dead = False  # Ou pode ser continue se quiser reiniciar o jogo
        continue  # Pula as atualizações do jogo e exibe o Game Over

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
      playerLeft = player.rect.x
      blockLeft = collide.rect.x + collide.rect.width
      if collide.rect.y-15 < playerFoot and collide.rect.y+15 > playerFoot:
        if not ((player.lastMove == -1 and playerRight-30 < collide.rect.x) or (player.lastMove == 1 and playerLeft+30 > collide.rect.x+collide.rect.width)):
          bottomCollide = True
      elif playerHead+15 > blockBottom and playerHead -15 < blockBottom:
        if not ((player.lastMove == -1 and playerRight-30 < collide.rect.x) or (player.lastMove == 1 and playerLeft+30 > collide.rect.x+collide.rect.width)):
          topCollide = True
      elif playerRight+15 > collide.rect.x and playerRight-15 < collide.rect.x: 
        rightCollide = True
      elif blockLeft +15 > player.rect.x and blockLeft-15 < player.rect.x:
        leftCollide = True
    player.bottomCollide = bottomCollide
    player.topCollide = topCollide
    player.leftCollide = leftCollide
    player.rightCollide = rightCollide

    if inicio_jogo:
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
            # hitSound.set_volume(1)
            # hitSound.play()
        elif key[pygame.K_e] and player.currentStatus != "attack" and not player.currentStatus == 'death' and player.currentStatus != "block":
          player.defense()
        elif player.bottomCollide and not player.currentStatus == 'attack' and not player.currentStatus == 'death' and player.currentStatus != 'block' and not player.currentStatus == 'hurt':
            player.xSpeed = 0
            player.changeStatus('idle')

        if key[pygame.K_SPACE] and not player.currentStatus == 'death':
            player.jump()
    




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


    pygame.display.flip()
  if restart:
    main()

main()

pygame.quit()