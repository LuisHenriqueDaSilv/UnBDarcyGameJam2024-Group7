from .DemonFly import DemonFly
from .DemonAxe import DemonAxe
from settings import SCREEN_HEIGHT

def createEnemies(spriteGroup):
  spriteGroup.add(DemonFly(550, 0, 100))
  demonAxeBase = DemonAxe(0, 0, 0)
  spriteGroup.add(DemonAxe(SCREEN_HEIGHT-128/2.5-demonAxeBase.rect.height, 0, 600))

  spriteGroup.add(DemonFly(230, 100, 200 ))
  spriteGroup.add(DemonFly(10, 350, 550))
  spriteGroup.add(DemonFly(-470, 300, 450))

  spriteGroup.add(DemonAxe(-790, 350, 550 ))

  spriteGroup.add(DemonFly(-1070, 0, 100))
  spriteGroup.add(DemonAxe(-1290, 200, 350))

  spriteGroup.add(DemonFly(-1820, 200, 300))