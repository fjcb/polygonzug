import random

class CVInput:

  def __init__(self):
    self.changed = False
    self.pointlist = list()
    self.width = 100
    self.height = 100
    self.point_a = (25, 25)
    self.point_b = (75, 75)

  def hasChanged(self):
    return self.changed

  def generateRandomPoints(self,width, height):
    self.pointlist = list()
    for i in range(0, 100):
      x = i * 50 % (width)
      y = random.randrange(0, height)
      self.pointlist.append((x, y))
