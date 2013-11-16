import pygame

class Render:

  def __init__(self, width, height):
    self.window = pygame.display.set_mode((width, height))

  def render(self, pointlist):
    self.window.fill((0, 0, 0))
    pygame.draw.lines(self.window, (255, 255, 255), False, pointlist, 3)
    pygame.display.flip()

  def toggleFullscreen(self):
    pygame.display.toggle_fullscreen()
