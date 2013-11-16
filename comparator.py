
#pointlist input and output is normalized [0,1]

class Comparator:

  def __init__(self, threshold = 0.001):
    self.threshold = threshold
    self.pointlist = list() #the ouput pointlist
    self.changed = True

  def update(self, new_pointlist):
    length = len(self.pointlist)
    new_length = len(new_pointlist)

    self.pointlist = new_pointlist
    #TODO:
    #compare input and ouput
    #point order consistency
    #set self.changed

  def mappedPoints(self, startpoint, width, height):
    mapped_pointlist = list()
    for item in self.pointlist:
      x = width * item[0] + startpoint[0]
      y = height * item[1] + startpoint[1]
      mapped_pointlist.append((x, y))
    return mapped_pointlist
