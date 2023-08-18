from settings import *
from grid import Grid
from blocks import *

pg.init()

screen = pg.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
logo = pg.image.load('LOGO.png')
bg_color = (30, 53, 105)

pg.display.set_icon(logo)
pg.display.set_caption("Matt's Tetris")

clock = pg.time.Clock()

on = True

grid = Grid()
#grid.print_grid()
block = LBlock()

while on:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
  
  #Drawing
  screen.fill(bg_color)
  grid.draw(screen)
  block.draw(screen)
  
  pg.display.update()
  clock.tick(60)
  
