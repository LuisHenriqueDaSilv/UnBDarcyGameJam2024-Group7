import pygame


pygame.init()
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

player = pygame.Rect(250, 350, 100, 100)

clock = pygame.time.Clock()

running = True
while running:

  clock.tick(120)
  screen.fill((0, 0, 0))

  pygame.draw.rect(screen, (255, 0, 0), player)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  key = pygame.key.get_pressed()
  if key[pygame.K_a]:
    player.move_ip(-1, 0)
  elif key[pygame.K_d]:
    player.move_ip(1, 0)
    

  pygame.display.update()

pygame.quit()