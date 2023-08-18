from settings import *
from colors import Colors
class Grid:
  def __init__(self):
    self.num_rows = 20
    self.num_cols = 10
    self.cell_size = 30
    self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
    self.colors = Colors.get_cell_colors()
    
  def print_grid(self):
    for row in range(self.num_rows):
      for col in range(self.num_cols):
        print(self.grid[row][col], end = " ")
      print()
   
  def draw(self, screen):
    for row in range(self.num_rows):
      for col in range(self.num_cols):
        cell_value = self.grid[row][col]
        cell_rect = pg.Rect(col*self.cell_size, row*self.cell_size, 
                            self.cell_size-1, self.cell_size-1)
        pg.draw.rect(screen, self.colors[cell_value], cell_rect)
    
  