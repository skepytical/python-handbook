import pygame
import numpy as np
import random

width, height  = 10, 20
grain_size = 30
proportion = 40
screen_size = width * proportion, height * proportion
columns, rows = screen_size[0] // grain_size, screen_size[1] // grain_size 

colors = {
  0: (0, 0, 0),        
  1: (0, 255, 255),    
  2: (255, 165, 0),    
  3: (0, 0, 255),      
  4: (255, 255, 0),    
  5: (128, 0, 128)
}


shapes = [
  [[1, 1, 1, 1]],
  [[1, 1], [1, 1]],
  [[0, 1, 0], [1, 1, 1]]
]

def main():
  pygame.init()
  screen = pygame.display.set_mode(screen_size)
  clock = pygame.time.Clock()
  grid = np.zeros((rows, columns), dtype=np.uint8)

  speed = 20
  frame = 0
  sandmino = create_sandmino()

  running = True
  while running:
    frame += 1
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_LEFT:
          sandmino["x"] -= 1
          if collision(sandmino, grid): 
            sandmino["x"] += 1
       if event.key == pygame.K_RIGHT:
            sandmino["x"] += 1
            if collision(sandmino, grid):
              sandmino["x"] -= 1
       if event.key == pygame.K_DOWN:
            sandmino["y"] += 1
            if collision(sandmino, grid):
              sandmino["y"] -= 1
       if event.key == pygame.K_UP:
          old_shape = sandmino["shape"]
          sandmino["shape"] = np.rot90(sandmino["shape"])
          if collision(sandmino, grid):
            sandmino["shape"] = old_shape #undo if collision
       if event.key == pygame.K_SPACE: 
          while not collision(sandmino, grid):
            sandmino["y"] += 1
          sandmino["y"] -= 1
          if sandmino["y"] <= 0:
            grid.fill(0)
          else:
            to_sand(sandmino, grid)
            clear_sand(grid)

          sandmino = create_sandmino()      

    if frame % speed == 0:
      sandmino["y"] += 1
      if collision(sandmino, grid):
        sandmino["y"] -= 1
        
        if sandmino["y"] <= 0:
          grid.fill(0)
        else:
          to_sand(sandmino, grid)
          clear_sand(grid)
        
        sandmino = create_sandmino()


    for y in range(rows - 2, -1, -1):
      indices = np.where(grid[y] > 0)[0]
      for x in indices:
        c = grid[y, x]
        if grid[y+1, x] == 0:
          grid[y+1, x], grid[y, x] = c, 0
        elif x > 0 and grid[y+1, x-1] == 0:
          grid[y+1, x-1], grid[y, x] = c, 0
        elif x < columns - 1 and grid[y+1, x+1] == 0:
          grid[y+1, x+1], grid[y, x] = c, 0

    pixels = np.zeros((rows, columns, 3), dtype=np.uint8)
    for colork, colorv in colors.items():
      if colork > 0:
        pixels[grid == colork] = colorv

    shape = sandmino["shape"]
    color = colors[sandmino["color"]]
    for ry, row in enumerate(shape):
      for rx, cell in enumerate(row):
        if cell:
          py, px = sandmino["y"] + ry, sandmino["x"] + rx
          if 0 <= py < rows and 0 <= px < columns:
            pixels[py, px] = color


    surface = pygame.surfarray.make_surface(pixels.swapaxes(0, 1))
    screen.fill((0, 0, 0))
    screen.blit(pygame.transform.scale(surface, screen_size), (0, 0))
    pygame.display.flip()
    clock.tick(60)
  pygame.quit()

def create_sandmino():
  return {
   "shape": np.array(random.choice(shapes)),
   "x": columns // 2 - 2,
   "y": 0,
   "color": random.randint(1, 5)
  }

def to_sand(piece, grid):
  shape = piece["shape"]
  color = piece["color"]
  for ry, row in enumerate(shape):
    for rx, cell in enumerate(row):
      if cell:
        # sand particles
        sy, sx = piece["y"] + ry, piece["x"] + rx
        if 0 <= sy < rows and 0 <= sx < columns:
          grid[sy, sx] = color 

def collision(piece, grid):
  shape = piece['shape']
  for ry, row in enumerate(shape):
    for rx, cell in enumerate(row):
      if cell:
        sy, sx = piece['y'] + ry, piece['x'] + rx
        if sy >= rows or sx < 0 or sx >= columns or grid[sy, sx] > 0:
          return True
  return False

def clear_sand(grid):
  for color in range(1, 6):
    seeds = []
    seeds = [(y, 0) for y in range(rows) if grid[y, 0] == color]
    if not seeds:
      continue
      

    visited = set(seeds)
    queue = list(seeds)
    connected = list(seeds)
    found = False
    
    while queue:
      y1, x1 = queue.pop(0)    
      if x1 == columns - 1:
        found = True
     
      for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
          ny, nx = y1 + dy, x1 + dx
          if 0 <= ny < rows and 0 <= nx < columns:
            if (ny, nx) not in visited and grid[ny, nx] == color:
              visited.add((ny, nx))
              queue.append((ny, nx))
              connected.append((ny, nx)) 
    if found:
      for py, px in connected:
        grid[py, px] = 0



if __name__ == "__main__":
  main()









