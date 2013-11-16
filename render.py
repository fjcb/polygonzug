import pygame

class Render:

  def __init__(self, width, height):
    self.window = pygame.display.set_mode((width, height))

  def render(self, pointlist):
    self.window.fill((0, 0, 0))
    pygame.draw.aalines(self.window, (255, 255, 255), False, pointlist, True)
    pygame.display.flip()
