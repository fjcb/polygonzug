import random

#TODO: keep old data if point count is increased and add new points

class PointGenerator:

  def __init__(self):
    self.count = 10         #number of points to be rendered
    self.count_min = 10
    self.count_max = 100
    self.x_list = list()
    self.y_list = list()
    self.seeds = (0, 0)
    self.x_func_idx = 0
    self.y_func_idx = 0
    self.generators = {0 : self.generateRandom, 1 : self.equidistantValues}

  #generates tupel(x, y) list of x and y values
  def getPointList(self):
    pointlist = list()
    for i in range(0, self.count-1):
      pointlist.append((self.x_list[i], self.y_list[i]))
    return pointlist

  #distribution functions------------------------------
  #has to be called for x and y list
  def generateRandom(self):
    pointlist = list()
    for i in range(0, self.count):
      pointlist.append(random.random())
    return pointlist

  def equidistantValues(self):
    pointlist = list()
    for i in range(0, self.count):
      pointlist.append(i * (1.0 / self.count))
    return pointlist
  #distribution functions------------------------------

  def incCount(self):
    self.count += 10
    if self.count > self.count_max:
      self.count = self.count_max
    self.countChanged()

  def decCount(self):
    self.count -= 10
    if self.count < self.count_min:
      self.count = self.count_min
    self.countChanged()

  def changeXFunc(self):
    self.x_func_idx += 1
    if self.x_func_idx >= len(self.generators):
      self.x_func_idx = 0
    self.x_list = self.generators[self.x_func_idx]()

  def changeYFunc(self):
    self.y_func_idx +=1
    if self.y_func_idx >= len(self.generators):
      self.y_func_idx = 0
    self.y_list = self.generators[self.y_func_idx]()

  def countChanged(self):
    self.x_list = self.generators[self.x_func_idx]()
    self.y_list = self.generators[self.y_func_idx]()
