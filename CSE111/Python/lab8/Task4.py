class Student:
  total_student=0
  Bracu_students=0
  other_students=0

  def __init__(self,name,department,institution="BRAC University"):
    self.name=name
    self.department=department
    self.institution=institution
    Student.total_student+=1
    if self.institution=="BRAC University":
      Student.Bracu_students+=1


    else:
      Student.other_students+=1

  @classmethod
  def createStudent(cls,name,department,institution="BRAC University"):

    # if institution!="BRAC University":
    #   cls.other_students+=1
    return cls(name,department,institution)

  @classmethod
  def printDetails(cls):
    print(f"Total Student(s): {cls.total_student}")
    print(f"BRAC University Student(s): {cls.Bracu_students}")
    print(f"Other Institution Student(s): {cls.other_students}")


  def individualDetail(self):
    print(f"Name: {self.name}")
    print(f"Department: {self.department}")
    print(f"Institution: {self.institution}")



Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()
