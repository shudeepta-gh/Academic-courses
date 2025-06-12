import math
class TwoDVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add2DVectors(self, *vectors):
        for i in vectors:
            self.x += i.x
            self.y += i.y
    def print2DVector(self):
        if self.y >= 0:
            y = "+ "+str(self.y)
        else:
            y = str(self.y)
        print(f"{self.x}i {y}j")


class ThreeDVector(TwoDVector):
  def __init__(self,x,y,z):
    super().__init__(x,y)

    self.z=z


  def add3DVectors(self,*vectors):
    for vector in vectors:
      super().add2DVectors(vector)
      self.z += vector.z



  def print3DVector(self):
      if self.x>=0:
            x = "+ "+str(self.x)
      else:
            x = str(self.x)

      if self.y>=0:
            y = "+ "+str(self.y)
      else:
            y = str(self.y)

      if self.z>=0:
            z = "+ "+str(self.z)
      else:
            z = str(self.z)
      print(f"{x}i + {y}j {z}k")


  def multiplyScalar(self,scaler):
      self.x*=scaler
      self.y*=scaler
      self.z*=scaler



  def calculateLength(self):
    length=math.sqrt((self.x**2)+(self.y**2)+(self.z**2))
    return length



TwoDV1 = TwoDVector(5, 6)
TwoDV2 = TwoDVector(3, 7)
TwoDV3 = TwoDVector(1, 8)
print("===============")
TwoDV1.add2DVectors(TwoDV2, TwoDV3)
TwoDV1.print2DVector()
print("===============")
ThreeDV1 = ThreeDVector(5, 6, 1)
ThreeDV2 = ThreeDVector(1, 9, -7)
ThreeDV3 = ThreeDVector(8, 2, 4)
print("===============")
ThreeDV1.add3DVectors(ThreeDV2,ThreeDV3)
ThreeDV1.print3DVector()
print("===============")
ThreeDV1.multiplyScalar(3)
ThreeDV1.print3DVector()
print("===============")
print(ThreeDV1.calculateLength())
