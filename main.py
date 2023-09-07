from settings import *
from game import Game

pg.init()

screen = pg.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
logo = pg.image.load('LOGO.png')
bg_color = (30, 53, 105)

pg.display.set_icon(logo)
pg.display.set_caption("Matt's Tetris")

font = pg.font.Font(None, 70)
font1 = pg.font.Font(None, 40) 

title = "TETRIS"
title_surface = font.render(title, True, (255, 255, 255))
title_rect = title_surface.get_rect()
title_rect.center = (GRID_WIDTH / 2, 35)

score = "score"
score_surface = font1.render(score, True, (255, 255, 255))
score_rect = score_surface.get_rect()
score_rect.center = (120, 470)

level = "level"
level_surface = font1.render(level, True, (255, 255, 255))
level_rect = level_surface.get_rect()
level_rect.center = (118, 545)

lines = "lines"
lines_surface = font1.render(lines, True, (255, 255, 255))
lines_rect = lines_surface.get_rect()
lines_rect.center = (118, 615)

hold = "hold"
hold_surface = font1.render(hold, True, (255, 255, 255))
hold_rect = hold_surface.get_rect()
hold_rect.center = (115, 90)

next_piece = "next"
next_surface = font1.render(next_piece, True, (255, 255, 255))
next_rect = next_surface.get_rect()
next_rect.center = (GRID_WIDTH - 125, 90)

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
      
      elif event.key == pg.K_r and game.game_over == False:
        game.reset()
      
      elif event.key == pg.K_UP and game.game_over == False:
        game.rotate()
        
      elif event.key == pg.K_c and game.game_over == False:
        game.hold_block()
      
      '''
      
      
      if event.key == pg.K_LEFT and game.game_over == False:
        game.move_left()
      elif event.key == pg.K_RIGHT and game.game_over == False:
        game.move_right()
      elif event.key == pg.K_DOWN and game.game_over == False:
        game.move_down()
      '''
      
      
    
    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT] and game.game_over == False:
      game.move_left()
    
    if keys[pg.K_RIGHT] and game.game_over == False:
      game.move_right()
    
    if keys[pg.K_DOWN] and game.game_over == False:
      game.move_down()
    
    if event.type == GAME_UPDATE and game.game_over == False:
      game.move_down()    
  
  #Drawing
  
  lines_count = str(game.lines)
  lines_count_surface = font1.render(lines_count, True, (255, 255, 255))
  lines_count_rect = lines_count_surface.get_rect()
  lines_count_rect.center = (120, 648)
  
  score_count = str(game.score)
  score_count_surface = font1.render(score_count, True, (255, 255, 255))
  score_count_rect = score_count_surface.get_rect()
  score_count_rect.center = (120, 508)
  
  level_count = str(game.level)
  level_count_surface = font1.render(level_count, True, (255, 255, 255))
  level_count_rect = score_count_surface.get_rect()
  level_count_rect.center = (120, 578)
  
  
  grid_bg_color = (209, 209, 209)
  grid_bg_pos = (GRID_WIDTH/3.33, 70)
  grid_bg_size = (320, GRID_HEIGHT-100)
  
  info_hub_color = (73, 82, 252)
  info_hub_pos = (30, 450)
  info_hub_size = (180, 240)
  
  info_bar_color = (54, 54, 54)
  info_bar_pos = (45, 490)
  info_bar_size = (150, 35)
  
  hold_bg_pos = (30, 70)
  hold_bg_size = (180, 160)
  
  hold_hub_pos = (40, 110)
  hold_hub_size = (160, 110)
  
  next_bg_pos = (GRID_WIDTH - 220, 70)
  next_bg_size = (200, GRID_HEIGHT/2.2)
  
  next_hub_pos = (GRID_WIDTH - 210, 110)
  next_hub_size = (180, GRID_HEIGHT/2.6)
  
  
  screen.fill(bg_color)
  pg.draw.rect(screen, info_hub_color, (hold_bg_pos, hold_bg_size), 0, 20)
  pg.draw.rect(screen, info_bar_color, (hold_hub_pos, hold_hub_size), 0, 20)
  pg.draw.rect(screen, info_hub_color, (next_bg_pos, next_bg_size), 0, 20)
  pg.draw.rect(screen, info_bar_color, (next_hub_pos, next_hub_size), 0 ,20)
  pg.draw.rect(screen, info_hub_color, (info_hub_pos, info_hub_size), 0 , 20)
  pg.draw.rect(screen, info_bar_color, (info_bar_pos, info_bar_size), 0, 10)
  pg.draw.rect(screen, info_bar_color, ((45, 560), info_bar_size), 0, 10)
  pg.draw.rect(screen, info_bar_color, ((45, 630), info_bar_size), 0, 10)
  pg.draw.rect(screen, grid_bg_color, (grid_bg_pos, grid_bg_size), 0 , 5)
  
  game.draw(screen)
  screen.blit(next_surface, next_rect)
  screen.blit(hold_surface, hold_rect)
  screen.blit(score_surface, score_rect)
  screen.blit(title_surface, title_rect)
  screen.blit(level_surface, level_rect)
  screen.blit(lines_surface, lines_rect)
  screen.blit(lines_count_surface, lines_count_rect)
  screen.blit(score_count_surface, score_count_rect)
  screen.blit(level_count_surface, level_count_rect)
  
  pg.display.update()
  clock.tick(60)
  
