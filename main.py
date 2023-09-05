from settings import *
from game import Game

pg.init()

screen = pg.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
logo = pg.image.load('LOGO.png')
bg_color = (30, 53, 105)

pg.display.set_icon(logo)
pg.display.set_caption("Matt's Tetris")

font = pg.font.Font(None, 70)

title = "Tetris"
title_surface = font.render(title, True, (255, 255, 255))
title_rect = title_surface.get_rect()
title_rect.center = (GRID_WIDTH / 2, 35)

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
      
      if event.key == pg.K_r and game.game_over == False:
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
  
  #Drawing
  
  grid_bg_color = (209, 209, 209)
  grid_bg_pos = (GRID_WIDTH/3.33, 70)
  grid_bg_size = (320, GRID_HEIGHT-100)
  
  info_hub_color = (73, 82, 252)
  info_hub_pos = (30, 470)
  info_hub_size = (180, 220)
    
  screen.fill(bg_color)
  pg.draw.rect(screen, info_hub_color, (info_hub_pos, info_hub_size), 0 , 20)
  pg.draw.rect(screen, grid_bg_color, (grid_bg_pos, grid_bg_size), 0 , 5)
  game.draw(screen)
  screen.blit(title_surface, title_rect)
  
  pg.display.update()
  clock.tick(60)
  
