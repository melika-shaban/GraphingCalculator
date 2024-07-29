#ellie
import math 


def SideLengths(P): #calculates each side length of the polygon
  try: 
    side_lengths=[] #empty list to add side lenths to
    x=0
    while x<(len(P))-1: #this formula doesn't work when x gets to the last coordinate in the list, so it goes until the second last one
      new = math.dist(P[x], P[x+1])
      New = round(new, 4)
      side_lengths.append(New)  
      x=x+1
    if x==len(P)-1: #when x is at the last coordinate in the list...
      new = math.dist(P[x], P[0]) #takes the distance between the last point and first point because it is the last side length of the polygon when entered in order
      New = round(new, 4)
      side_lengths.append(New)    
    return(side_lengths) #return the list of sidelengths 
  except: 
    return("please enter appropriate coordinates")

def Perimeter(P): #calculates the perimeter of the polygon 
  SL=SideLengths(P) 
  total=0
  for x in range (0, (len(SL))): #goes through every side length in the list
    total= total + SL[x] #adds each to a total value counter
  return(total) #returns the total value after each point has been added 


def Regular_Polygon_Checker(P): #checks if the polygon is a "regular" polygon (all sides are the same length)
  lengths = SideLengths(P)
  for x in range (1, len(lengths)): #takes only above range 1 so that it can easily be compared to the point before it 
    if lengths[x] == lengths[x-1]: #if the side length and the one before it are equal for every side length...
      return True #then it is a regular polygon
    else: 
      return False 


class Polygons: #A parent class for all subclasses to have the attributes that all polygons have that need to be used (coordinates, sidelengths, perimeter, area)
  def __init__(self, P):
    self.P = P
    self.lengths = SideLengths(P) #finds sidelengths using SideLengths function
    self.perimeter = Perimeter(P)#finds perimeter using Perimeter function



class square(Polygons): 
  def __init__ (self, P):
    super().__init__(P)
    if Regular_Polygon_Checker(P) == True: #checks if the shape is a square just in case user clicked wrong button, or inputed points in the wrong order
      self.area = self.lengths[0]**2
    else:
      self.area =("This is not a square, please enter points in order or select correct shape.")



class rectangle(Polygons): 
  def __init__ (self, P):
    super().__init__(P)
    if self.lengths[0]==self.lengths[2] and self.lengths[1]==self.lengths[3]: #checks if both sets of the two sides parrallel to each other are equal in length
      self.area = self.lengths[0] * self.lengths[1] 
    else:
      self.area =("This is not a rectangle, please enter points in order or select correct shape.") #if it is not a rectangle, area is a message to user



class triangle(Polygons): 
  def __init__ (self, P):
    super().__init__(P)
    s = self.perimeter/2 #finds the semi-perimeter (half of the perimeter) to be used in the area equation
    self.area = round((math.sqrt(s*((s-self.lengths[0])*(s-self.lengths[1])*(s-self.lengths[2])))), 4) # finding the area of the triangle using the Heron's function





class parallelogram(Polygons): 
  def __init__ (self, P):
    super().__init__(P)
    if P[0][1]==P[1][1]: #if lines stay horizontal on the x axis and the base is the first two points inputed...
      PN = (P[3][0], P[0][1]) #the point used to calculate height is directly below the third point
      h = math.dist(P[3], PN) #calculates the height
      self.area = round((self.lengths[0]*h), 4) #calculates the area using base x height
    elif P[3][1]==P[0][1]: #if lines stay horizontal on the x axis and the base is not the first two points inputed...
      PN = (P[2][0], P[0][1]) #the point used to calculate the height is directly below the second point
      h = math.dist(P[2], PN)
      self.area = round((self.lengths[1]*h), 4) 
      #these two will work for any order of points because the bases are parallel and equal and the tilted sides are parallel and equal 
    elif P[3][0]==P[0][0]: #if the lines stay vertical on the y axis and the base is not the first two points inputed... 
      PN = (P[0][0], P[2][1]) #the point to calculate the height is the x coordinate of the first point and the y coordinate of the third point
      h = math.dist(P[2], PN)
      self.area = round((self.lengths[1]*h), 4)
    elif P[2][0]==P[3][0]: #if the lines stay vertical on the y axis and the base is the first two points inputed... 
      PN = (P[3][0], P[1][1]) #the point to calculate the height is the x coordinate of the last point and the y coordinate of the second point
      h = math.dist(P[1], PN)
      self.area = round((self.lengths[0]*h), 4)
    else: #if the base isn't straight along the x or y axis
      self.area = "cannot calculate area of this parallelogram. Best of luck." 





class hexagon(Polygons):
  def __init__ (self, P):
    super().__init__(P)
    P02 = math.dist(P[0], P[2]) #seperated the hexagon into 4 seperate triangles and P02, P25, P42 are the lengths of the lines used to seperate the triangles 
    P25 = math.dist(P[2], P[5])
    P42 = math.dist(P[4], P[2])
    s1 = (Perimeter([P[0], P[1], P[2]]))/2 #finding semi perimeter of the first triangle out of the 4 
    a1 = math.sqrt(s1*(s1-self.lengths[0])*(s1-self.lengths[1])*(s1-P02)) #finds the area of the first triangle using Heron's formula same as objects in the triangle class
    s2 = (Perimeter([P[5], P[2], P[0]]))/2 #process is repeated from above with the other 3 triangles, using appropriate variables
    a2 = math.sqrt(s2*(s2-self.lengths[5])*(s2-P02)*(s2-P25))
    s3 = (Perimeter([P[4], P[5], P[2]]))/2
    a3 = math.sqrt(s3*(s3-self.lengths[4])*(s3-P25)*(s3-P42))
    s4 = (Perimeter([P[3], P[2], P[4]]))/2
    a4 = math.sqrt(s4*(s4-self.lengths[3])*(s4-self.lengths[2])*(s4-P42))
    Area = a1 + a2 + a3 + a4 #the area is sum of all the 4 triangles 
    self.area=round(Area, 3) #decimals may go on forever depending on the hexagon, so it rounds to the first four




class octagon(Polygons):
  def __init__ (self, P):
    super().__init__(P)
    P20 = math.dist(P[2], P[0]) #seperated the octagon into 6 seperate triangles and P20, P27, P26, P25, P24 are the lengths of the lines used to seperate the triangles 
    P27 = math.dist(P[2], P[7]) 
    P26 = math.dist(P[2], P[6])
    P25 = math.dist(P[2], P[5])
    P24 = math.dist(P[2], P[4])
    s1 = (Perimeter([P[1], P[0], P[2]]))/2 #does the same theory as hexagons, just with more triangles
    a1 = math.sqrt(s1*(s1-self.lengths[0])*(s1-self.lengths[1])*(s1-P20))
    s2 = (Perimeter([P[0], P[2], P[7]]))/2
    a2 = math.sqrt(s2*(s2-self.lengths[7])*(s2-P20)*(s2-P27))
    s3 = (Perimeter([P[2], P[7], P[6]]))/2
    a3 = math.sqrt(s3*(s3-self.lengths[6])*(s3-P27)*(s3-P26))
    s4 = (Perimeter([P[2], P[5], P[6]]))/2
    a4 = math.sqrt(s4*(s4-self.lengths[5])*(s4-P25)*(s4-P26))
    s5 = (Perimeter([P[2], P[5], P[4]]))/2
    a5 = math.sqrt(s5*(s5-self.lengths[4])*(s5-P25)*(s5-P24))
    s6 = (Perimeter([P[4], P[3], P[2]]))/2
    a6 = math.sqrt(s6*(s6-self.lengths[3])*(s6-self.lengths[2])*(s6-P24))
    Area = a1 + a2 + a3 + a4 + a5 + a6 #adds the area of all the triangles
    self.area=round(Area, 2) #decimals may go on forever depending on the octagon, so it rounds to the first four
