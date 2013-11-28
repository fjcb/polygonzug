import pygame

#TODO: render the name of actual distribution function for user feedback

class Render:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.window = pygame.display.set_mode((width, height))
    pygame.font.init()
    self.font = pygame.font.Font(None, 48)
    self.colorBack = (255, 255, 255)
    self.colorFore = (0,0,0)

  #pointlist is normalized in [0,1], rect defines the area on the screen where the polyline will be rendered
  def render(self, pointlist, rect, border, x_idx, y_idx, count):
    #clear screen

    self.window.fill(self.colorBack)

    left_width = rect.left
    right_width = self.width - left_width - rect.width
    
    #display generator indexes
    text = self.font.render(str(x_idx), 1, self.colorFore)
    textpos = text.get_rect(centerx = left_width + 25, centery = self.height - 25)
    self.window.blit(text, textpos)
    
    text = self.font.render(str(y_idx), 1, self.colorFore)
    textpos = text.get_rect(centerx = self.width - left_width - 25, centery = self.height - 25)
    self.window.blit(text, textpos)

    text = self.font.render(str(count-1), 1, self.colorFore)
    textpos = text.get_rect(centerx = self.window.get_rect().centerx + 25, centery = 25)
    self.window.blit(text, textpos)
    
    #draw left and right black border
    pygame.draw.rect(self.window, (0,0,0), pygame.Rect(0, 0, left_width, self.height))
    pygame.draw.rect(self.window, (0,0,0), pygame.Rect(self.width - right_width, 0, self.width, self.height))

    #convert pointlist to screenspace with respect to the border
    render_pointlist = list()
    for item in pointlist:
      x = (rect.width - 2 * border) * item[0] + rect.left + border
      y = (rect.height - 2 * border) * item[1] + rect.top + border
      render_pointlist.append((x, y))

    #draw polyline
    pygame.draw.lines(self.window, self.colorFore, False, render_pointlist, 3)

    #display everything
    pygame.display.flip()

  def swapColors(self):
      color = self.colorBack
      self.colorBack = self.colorFore
      self.colorFore = color

  def credits(self):
    print "Fritz Jacob & Robert Kuhfss"
  
  def toggleFullscreen(self):
    pygame.display.toggle_fullscreen()

