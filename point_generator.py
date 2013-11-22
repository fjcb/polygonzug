import random
import math

#TODO: keep old data if point count is increased and add new points

class PointGenerator:

  def __init__(self):
    self.count        = 4  #number of points to be rendered
    self.count_min    = 4
    self.count_max    = 51
    self.count_amount = 1
    self.x_list       = list()
    self.y_list       = list()
    self.seeds        = (0, 0)
    self.x_func_idx   = 0
    self.y_func_idx   = 0
    self.generators   = { 0:self.equidistantValues, 1:self.generateRandom, 2:self.quadrantLove, 3:self.sinus, 4:self.cosin, 5:self.randone, 6:self.modulo }

  #generates tupel(x, y) list of x and y values
  def getPointList(self):
    pointlist = list()
    for i in range(0, self.count):
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
      pointlist.append(i * (1.0 / (self.count-1)))
    return pointlist

  def quadrantLove(self):
    pointlist = list()
    old = 0
    for i in range(0, self.count):
      new = random.random()
      if old < 0.5:
        new = 1 - new / 2 # new is > 0.5
      else:
        new = new / 2 # new is < 0.5
      pointlist.append(new)
      old = new
    return pointlist

  def sinus(self):
    pointlist = list()
    wave = random.randint(4,15)#2,6)*math.pi;
    for i in range(0, self.count):
      pointlist.append((math.sin(wave * i * (1.0 / (self.count-1)))+1)/2)
    return pointlist

  def cosin(self):
    pointlist = list()
    wave = random.randint(4,15)#2,6)*math.pi;
    for i in range(0, self.count):
      pointlist.append((math.cos(wave * i * (1.0 / (self.count-1)))+1)/2)
    return pointlist

  def randone(self):
    pointlist = list()
    rand = random.random()
    for i in range(0, self.count):
      pointlist.append(rand + math.sin(random.random()*2*math.pi)*0.1)
    return pointlist

  def modulo(self):
    pointlist = list()
    step = random.random()
    counter = random.random()
    for i in range(0, self.count):
      pointlist.append(counter % 1)
      counter += step
    return pointlist
        
  #distribution functions------------------------------

  def incCount(self):
    self.count += self.count_amount
    if self.count > self.count_max:
      self.count = self.count_max
    self.countChanged()

  def decCount(self):
    self.count -= self.count_amount
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
