import random
import math

#TODO: keep old data if point count is increased and add new points

class PointGenerator:

  def __init__(self):
    self.count        = 12  #number of points to be rendered
    self.count_min    = 4
    self.count_max    = 100
    self.count_amount = 1
    self.x_list       = list()
    self.y_list       = list()
    self.seeds        = (0, 0)
    self.x_func_idx   = 0
    self.y_func_idx   = 0
    self.generators   = { 0:self.equidistantValues,
                          1:self.generateRandom,
                          2:self.frieder,
                          3:self.modulo,
                          4:self.noise,
                          5:self.quadrantLove,
                          6:self.sinus,
                          7:self.randone,
                          8:self.fibonacci,
                          9:self.expo
                          }

  #generates tupel(x, y) list of x and y values
  def getPointList(self):
    pointlist = list()
    for i in range(0, self.count):
      pointlist.append((self.x_list[i], self.y_list[i]))
    return pointlist

  #distribution functions------------------------------
  #has to be called for x and y list
  
  def equidistantValues(self):
    pointlist = list()
    for i in range(0, self.count):
      pointlist.append(i * (1.0 / (self.count-1)))
    return pointlist

  def generateRandom(self):
    pointlist = list()
    for i in range(0, self.count):
      pointlist.append(random.random())
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

  def fibonacci(self):
    pointlist = list()
    for i in range(0, self.count):
      if i >= 2:
        new = pointlist[i-1] + pointlist[i-2]
        if new > 1:
          new = new / 42
        pointlist.append(new % 1)
      else:
        pointlist.append(random.random())
    return pointlist

  def expo(self):
    points = list()
    for i in range(0, self.count):
      points.append((math.exp(i*0.42) / 42) % 1)
    return points

  def noise(self):
    points = list()
    points.append(random.random())
    for i in range(0, self.count - 1):
      points.append((points[i - 1] + random.random() * 0.2 - 0.1) % 1)
    return points

  def frieder(self):
    points = list()
    name = ['F', 'R', 'I', 'E', 'D', 'E', 'R', 'N', 'A', 'K', 'E']
    for i in range(0, self.count):
      points.append((((ord(name[i % len(name)])-60) * 0.1)+0.05) % 1)
    return points
  
  def primes(self):
    pointlist = list()
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
              31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
              73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
              127, 131, 137, 139, 149, 151, 157, 163, 167,
              173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251, 257, 263, 269,
              271, 277, 281, 283, 293, 307, 311]
    for i in range(0, self.count):
      pointlist.append((primes[i] * 0.001) % 1)
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
