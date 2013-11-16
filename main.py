import sys
import pygame

from render import Render
from cv_input import CVInput
from comparator import Comparator

#globals
g_width = 1024
g_height = 768
g_threshold = 0.001

#main setup
render = Render(g_width, g_height)
cv_input = CVInput()
comparator = Comparator(g_threshold)

#main loop
while True:
  for event in pygame.event.get():
    #key input
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_n:
        cv_input.generateRandomPoints()                                 #read new image
        comparator.update(cv_input.pointlist)                           #compare new and old pointlist and update output-pointlist

        if comparator.changed:
          render.render(comparator.mappedPoints((100,100), 500, 300))   #render updated pointlist if it has changed

      if event.key == pygame.K_f:
        render.toggleFullscreen()

      if event.key == pygame.K_ESCAPE:
        sys.exit(0)

    if event.type == pygame.QUIT:
      sys.exit(0)


