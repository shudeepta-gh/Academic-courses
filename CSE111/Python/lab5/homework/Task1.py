class Student:
  def __init__(self,name,cgpa=None,credit=9,dept="CSE"):
    self.name=name
    self.cgpa=cgpa
    self.credit=credit
    self.dept=dept

  def checkScholarshipEligibility(self):
     self.status=""

     if self.cgpa>=3.5 and self.credit>10:
      if self.cgpa>=3.7:
        print(f"{self.name} is eligible for Merit-based scholarship.")
        self.status+="Merit-based scholarship"
      else:
        if 3.5<=self.cgpa<3.7:
          print(f"{self.name} is eligible for Need-based scholarship.")
          self.status+="Need-based scholarship"


     else:
        print(f"{self.name} is not eligible for scholarship.")
        self.status+="No scholarship"


  def showDetails(self):
    print(f"Name:{self.name}")
    print(f"Department:{self.dept}")
    print(f"CGPA:{self.cgpa}")
    print(f"Number of Credits:{self.credit}")
    print(f"Scholarship Status:{self.status}")


print('--------------------------')
std1 = Student("Alif", 3.99, 12)
print('--------------------------')
std1.checkScholarshipEligibility()
print('--------------------------')
std1.showDetails()
print('--------------------------')
std2 = Student("Mim", 3.4)
std3 = Student("Henry", 3.5, 15,"BBA")
print('--------------------------')
std2.checkScholarshipEligibility()
print('--------------------------')
std3.checkScholarshipEligibility()
print('--------------------------')
std2.showDetails()
print('--------------------------')
std3.showDetails()
print('--------------------------')
std4 = Student("Bob", 4.0, 6, "CSE")
print('--------------------------')
std4.checkScholarshipEligibility()
print('--------------------------')
std4.showDetails()
