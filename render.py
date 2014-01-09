# -*- coding: cp1252 -*-
import pygame
import time

#TODO: render the name of actual distribution function for user feedback # DONE ;) -R @sonntag

class Render:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.window = pygame.display.set_mode((width, height))
    pygame.font.init()
    self.font = pygame.font.Font("fonts/crux.ttf", 56) #pygame.font.match_font("Arial")
    self.colorBack = (255, 255, 255)
    self.colorFore = (0,0,0)
    self.names        = { 0:"lines",
                          1:"randm",
                          2:"names",
                          3:"modul",
                          4:"noise",
                          5:"quadr",
                          6:"sinus",
                          7:"slice",
                          8:"fibon",
                          9:"expon"
                          }

  #pointlist is normalized in [0,1], rect defines the area on the screen where the polyline will be rendered
  def render(self, pointlist, rect, border, x_idx, y_idx, count):
    #clear screen

    self.window.fill(self.colorBack)

    left_width = rect.left
    right_width = self.width - left_width - rect.width
    
    #display generator indexes
    text = self.font.render("x: " + self.names[x_idx], 1, self.colorFore)
    textpos = text.get_rect(centerx = left_width + 100, centery = self.height - 50)
    self.window.blit(text, textpos)
    
    text = self.font.render("y: " + self.names[y_idx], 1, self.colorFore)
    textpos = text.get_rect(centerx = self.width - left_width - 100, centery = self.height - 50)
    self.window.blit(text, textpos)

    text = self.font.render("amount: " + str(count-1), 1, self.colorFore)
    textpos = text.get_rect(centerx = self.window.get_rect().centerx, centery = 50)
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

  def save(self):
    stamp = int(time.time())
    pygame.image.save(self.window, "captures/capture_{0}.jpeg".format(stamp))
    
  def credits(self):
    rect = pygame.Rect((self.width-self.height)/2, 0, self.height, self.height)
    left_width = rect.left
    right_width = self.width - left_width - rect.width

    text = pygame.font.Font("fonts/crux.ttf", 77).render("PIPYLON", 1, self.colorFore)
    textpos = text.get_rect(centerx = self.window.get_rect().centerx, centery = self.height/2 - 25)
    #pygame.draw.rect(self.window, self.colorBack, textpos) #background color?
    self.window.blit(text, textpos)
    
    text = pygame.font.Font("fonts/crux.ttf", 63).render("Fritz Jacob & Robert Kuhfß", 1, self.colorFore)
    textpos = text.get_rect(centerx = self.window.get_rect().centerx, centery = self.height/2 + 25)
    #pygame.draw.rect(self.window, self.colorBack, textpos) #background color?
    self.window.blit(text, textpos)
    
    pygame.display.flip()
