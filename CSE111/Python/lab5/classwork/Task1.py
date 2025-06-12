class Student:
  def __init__(self,name,id,department="CSE"):
    self.name=name
    self.id=id
    self.department=department

  def dailyEffort(self,hour):
    self.hour=hour



  def printDetails(self):
    print(f"Name:{self.name}")
    print(f"ID:{self.id}")

    print(f"Department: {self.department}")
    print(f"Daily Effort: {self.hour} hour(s)")
    if self.hour<=2:
      print(f"Suggestion:Should give more effort!")

    elif 2<self.hour<=4:
      print(f"Suggestion:Keep up the good work!")

    else:
      print(f"Suggestion:Excellent! Now motivate others.")



harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()
