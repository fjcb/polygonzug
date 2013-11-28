import sys
import time
import pygame

from render import Render
from point_generator import PointGenerator

#globals
g_width = 1024
g_height = 768
g_time = 0

def repaint():
  global render
  global point_generator
  render.render(point_generator.getPointList(), pygame.Rect((g_width-g_height)/2, 0, g_height, g_height), 10, point_generator.x_func_idx, point_generator.y_func_idx, point_generator.count)

def ping():
  global g_time
  g_time = time.clock()

#main setup
render = Render(g_width, g_height)
point_generator = PointGenerator()

pygame.mouse.set_visible(False)

#create and draw first polyline
point_generator.changeXFunc()
point_generator.changeYFunc()
repaint()

pygame.mouse.set_visible(False)


#main loop
while True:
  try:

    #check idle time
    if time.clock() - g_time > 5 * 60:
      render.credits()
      ping()
      
    for event in pygame.event.get():

      #update idle time
      ping()
      
      #key input
      if event.type == pygame.KEYUP:
        
        if event.key == pygame.K_f:
          render.toggleFullscreen()

        if event.key == pygame.K_ESCAPE:
          sys.exit(0)

      #if event.type == pygame.MOUSEMOTION:
      
      #check mouse inputs
      if event.type == pygame.MOUSEBUTTONDOWN:

        point_generator.seeds = pygame.mouse.get_rel()

        if event.dict['button'] == 1:
          #left mouse button
          point_generator.changeXFunc()
          repaint()
        elif event.dict['button'] == 2:
          #mouse wheelbutton
          render.swapColors()
          repaint()
        elif event.dict['button'] == 3:
          #right mouse button
          point_generator.changeYFunc()
          repaint()
        elif event.dict['button'] == 4:
          #mouse wheel up
          point_generator.incCount()
          repaint()
        elif event.dict['button'] == 5:
          #mouse wheel down
          point_generator.decCount()
          repaint()

      if event.type == pygame.QUIT:
        sys.exit(0)
        
  except Exception as e:
    print e
    # restart
    point_generator = PointGenerator()
    point_generator.changeXFunc()
    point_generator.changeYFunc()
    repaint()

