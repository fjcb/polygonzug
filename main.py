import sys
import pygame

from render import Render
from cv_input import CVInput

#globals
g_width = 1024
g_height = 768

#main setup
render = Render(g_width, g_height)
cv_input = CVInput()

#main loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_n:
        cv_input.generateRandomPoints(g_width, g_height)
        render.render(cv_input.pointlist)

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_ESCAPE:
        sys.exit(0)

    if event.type == pygame.QUIT:
      sys.exit(0)
