class Sphere:
  def __init__(self,sphere_id,r=1,color="White"):
    self.sphere_id=sphere_id
    self.radius=r
    self.color=color
    self.volume=(4/3)*3.1416*((self.radius)**3)

  def printDetails(self):
    print(f"Sphere ID:{self.sphere_id}")
    print(f"Color:{self.color}")
    print(f"Volume:{self.volume}")


  def merge_sphere(self,*spheres):
    print("Spheres are being merged")
    for sphere in spheres:
      self.volume+=sphere.volume

      if sphere.color!=self.color:
        self.color="Mixed color"


sphere1 = Sphere("Sphere 1")
print("1***************")
sphere1.printDetails()
print("2***************")
sphere2 = Sphere("Sphere 2", 3)
print("3***************")
sphere2.printDetails()
print("4***************")
sphere3 = Sphere("Sphere 3", 2)
print("5***************")
sphere3.printDetails()
print("6***************")
sphere3.merge_sphere(sphere1,sphere2)
print("7***************")
sphere3.printDetails()
print("8***************")
sphere4 = Sphere("Sphere 4", 5, "Purple")
print("9***************")
sphere4.merge_sphere(sphere3)
print("10***************")
sphere4.printDetails()
