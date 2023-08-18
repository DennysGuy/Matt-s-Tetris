class Colors:
  gray = (28, 28, 28)
  green = (0, 255, 0)
  red = (255, 0 , 0)
  orange = (255, 127, 0)
  yellow = (255, 255, 0)
  purple = (128, 0, 128)
  cyan = (0, 255, 255)
  blue =(0, 0, 255)
  
  @classmethod
  def get_cell_colors(cls):
    return [cls.gray, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]