import pygame

#TODO: render the name of actual distribution function for user feedback

class Render:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.window = pygame.display.set_mode((width, height))

  #pointlist is normalized in [0,1], rect defines the area on the screen where the polyline will be rendered
  def render(self, pointlist, rect, border):
    #clear screen
    self.window.fill((255, 255, 255))

    #draw left and right black border
    left_width = rect.left
    right_width = self.width - left_width - rect.width
    pygame.draw.rect(self.window, (0, 0, 0), pygame.Rect(0, 0, left_width, self.height))
    pygame.draw.rect(self.window, (0, 0, 0), pygame.Rect(self.width - right_width, 0, self.width, self.height))

    #convert pointlist to screenspace with respect to the border
    render_pointlist = list()
    for item in pointlist:
      x = (rect.width - 2 * border) * item[0] + rect.left + border
      y = (rect.height - 2 * border) * item[1] + rect.top + border
      render_pointlist.append((x, y))

    #draw polyline
    pygame.draw.lines(self.window, (0, 0, 0), False, render_pointlist, 3)
    pygame.display.flip()

  def toggleFullscreen(self):
    pygame.display.toggle_fullscreen()

