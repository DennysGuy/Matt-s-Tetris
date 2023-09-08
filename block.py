from colors import Colors
from settings import *
from position import Position
class Block:
  def __init__(self, id):
    self.id = id
    self.cells = {}
    self.cell_size = 30
    self.row_offset = 0
    self.col_offset = 0
    self.rotation_state = 0
    self.colors = Colors.get_cell_colors()
  
  def move(self, rows, cols):
    self.row_offset += rows
    self.col_offset += cols
  
  def get_cell_positions(self):
    tiles = self.cells[self.rotation_state]
    moved_tiles = []
    for position in tiles:
      position = Position(position.row + self.row_offset, position.col + self.col_offset)
      moved_tiles.append(position)
    return moved_tiles
  
  
  def rotate_block(self):
    self.rotation_state += 1
    if self.rotation_state == len(self.cells):
        self.rotation_state = 0
        
  
  def undo_rotation(self):
    self.rotation_state -= 1
    if self.rotation_state == -1:
      self.rotation_state = len(self.cells)-1


  def draw(self, screen, offset_x, offset_y):
    tiles = self.get_cell_positions()
    offset = 251
    
    for tile in tiles:
      tile_rect = pg.Rect(tile.col * self.cell_size + offset_x, tile.row * self.cell_size + offset_y,  
                          self.cell_size-1, self.cell_size-1)
      pg.draw.rect(screen, self.colors[self.id], tile_rect)
      
    
  
