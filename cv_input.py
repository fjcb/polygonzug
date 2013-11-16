import random

class CVInput:

  def __init__(self):
    self.pointlist = list()

  def generateRandomPoints(self):
    self.pointlist = list()
    for i in range(0, 100):
      x = random.random()
      y = random.random()
      self.pointlist.append((x, y))
