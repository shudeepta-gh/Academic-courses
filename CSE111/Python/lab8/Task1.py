class Student:
  ID=0
  def __init__(self,name,dept,age,cgpa):
    self.name=name
    self.dept=dept
    self.age=age
    self.cgpa=cgpa
    Student.ID+=1
    self.id=Student.ID


  @classmethod
  def from_String(cls,student_string):
    name,dept,age,cgpa=student_string.split("-")
    return cls(name,dept,int(age),float(cgpa))


  def showDetails(self):
      print(f"ID: {self.id}")
      print(f"Name: {self.name}")
      print(f"Department: {self.dept}")
      print(f"Age: {self.age}")
      print(f"CGPA: {self.cgpa}")



s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails()
