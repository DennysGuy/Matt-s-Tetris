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
GAME_UPDATE = pg.USEREVENT
pg.time.set_timer(GAME_UPDATE, 200)

on = True


while on:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()

    if event.type == pg.KEYDOWN:
      if game.game_over == True:
        game.game_over = False
        game.reset()
      
      if event.key == pg.K_LEFT and game.game_over == False:
        game.move_left()
      elif event.key == pg.K_RIGHT and game.game_over == False:
        game.move_right()
      elif event.key == pg.K_DOWN and game.game_over == False:
        game.move_down()
      elif event.key == pg.K_UP and game.game_over == False:
        game.rotate()
    
    if event.type == GAME_UPDATE and game.game_over == False:
      game.move_down()    
  
  if (game.game_over == True):
    print("True")
  else:
    print("False")        
    
  #Drawing
  screen.fill(bg_color)
  game.draw(screen)
  
  pg.display.update()
  clock.tick(60)
  
