import sys
import pygame

from render import Render
from point_generator import PointGenerator

#globals
g_width = 1024
g_height = 768

#main setup
render = Render(g_width, g_height)
point_generator = PointGenerator()

def repaint():
  global render
  global point_generator
  render.render(point_generator.getPointList(), pygame.Rect(128, 0, 768, 768), 10)

#create and draw first polyline
point_generator.changeXFunc()
point_generator.changeYFunc()
repaint()

pygame.mouse.set_visible(False)

#main loop
while True:
  for event in pygame.event.get():
    #key input
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_f:
        render.toggleFullscreen()

      if event.key == pygame.K_ESCAPE:
        sys.exit(0)

    #check mouse inputs
    if event.type == pygame.MOUSEBUTTONDOWN:
      point_generator.seeds = pygame.mouse.get_rel()

      if event.dict['button'] == 1:
        #left mouse button
        point_generator.changeXFunc()
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


