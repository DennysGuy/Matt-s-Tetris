from settings import *
from game import Game

pg.init()

screen = pg.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
logo = pg.image.load('LOGO.png')
bg_color = (30, 53, 105)

pg.display.set_icon(logo)
pg.display.set_caption("Matt's Tetris")

clock = pg.time.Clock()

game = Game()

on = True


while on:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
  
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_LEFT:
        game.current_block.move_left()
      elif event.key == pg.K_RIGHT:
        game.current_block.move_right()
      elif event.key == pg.K_DOWN:
        game.current_block.move_down()
    
  #Drawing
  screen.fill(bg_color)
  game.draw(screen)
  
  pg.display.update()
  clock.tick(60)
  
